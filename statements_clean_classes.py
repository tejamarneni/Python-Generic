import re
import os
import pdfplumber
import pandas as pd

class SavorProcessor:
    def __init__(self, pattern: str, year_config: dict):
        self.pattern = pattern
        self.year_config = year_config
        # Regex attributes
        self.phone_pattern = r'\d{3}[-\s]\d{3}[-\s]\d{4}'
        self.junk_pattern = r'#\d+|\d{3,}'
        self.state_pattern = r'(.*)\s+([A-Z]{2})$'

    def extract_expected_total(self, path: str) -> float:
        """Finds the 'official' total reported by the bank on page 1."""
        try:
            with pdfplumber.open(path) as pdf:
                # Summary is usually on the first page
                text = pdf.pages[0].extract_text()
                # Searches for 'Total Purchases' followed by an amount
                match = re.search(r'Total Purchases\s+\$?([\d,]+\.\d{2})', text)
                if match:
                    return float(match.group(1).replace(',', ''))
        except Exception as e:
            print(f"  ! Could not read summary for {os.path.basename(path)}: {e}")
        return None

    def _extract_raw_rows(self, path: str, year: int, pages: list) -> pd.DataFrame:
        all_transactions = []
        with pdfplumber.open(path) as pdf:
            for p_idx in pages:
                if p_idx >= len(pdf.pages): continue
                page = pdf.pages[p_idx]
                words = page.extract_words()
                if not words: continue
                
                df_words = pd.DataFrame(words)
                page_lines = df_words.groupby("top")["text"].apply(lambda x: " ".join(x))
                
                for line in page_lines:
                    matches = re.findall(self.pattern, line)
                    for m in matches:
                        all_transactions.append({
                            "Source": os.path.basename(path),
                            "Date": f"{m[0]}/{year}",
                            "Full_Description": m[1].strip(),
                            "Amount": m[2]
                        })
        return pd.DataFrame(all_transactions)

    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty: return df
        # Clean Amount
        df["Amount"] = df["Amount"].str.replace("$", "", regex=False).str.replace(",", "").astype(float)
        # Clean Description
        df['Full_Description'] = df['Full_Description'].str.replace(self.phone_pattern, '', regex=True)
        df['Full_Description'] = df['Full_Description'].str.replace(self.junk_pattern, '', regex=True)
        # Extract State
        extracted = df['Full_Description'].str.extract(self.state_pattern)
        df['State'] = extracted[1]
        df['Full_Description'] = extracted[0].fillna(df['Full_Description']).str.strip().str.title()
        return df

    def process_file(self, path: str, year: int):
        pages = self.year_config.get(year, [8, 9, 10, 11])
        raw_df = self._extract_raw_rows(path, year, pages)
        return self._clean_data(raw_df)


class BatchManager:
    def __init__(self, folder: str, processor: SavorProcessor):
        self.folder = folder
        self.processor = processor
        self.all_dfs = []
        self.audit_log = []

    def run_pipeline(self):
        for filename in os.listdir(self.folder):
            if not filename.lower().endswith(".pdf"): continue
            
            year_match = re.search(r'(\d{4})', filename)
            if not year_match: continue
            
            year = int(year_match.group(1))
            path = os.path.join(self.folder, filename)
            
            # 1. Expected from Bank
            expected = self.processor.extract_expected_total(path)
            
            # 2. Extract and Clean
            df = self.processor.process_file(path, year)
            
            # 3. Validate
            status = "No Summary Found"
            if not df.empty and expected is not None:
                calc = round(df['Amount'].sum(), 2)
                if calc == round(expected, 2):
                    status = "✅ PASS"
                else:
                    status = f"❌ FAIL (Diff: {round(expected - calc, 2)})"
            
            self.audit_log.append({"File": filename, "Status": status})
            print(f"File: {filename} | {status}")
            
            if not df.empty:
                self.all_dfs.append(df)
                df.to_csv(os.path.join(self.folder, f"cleaned_{year}.csv"), index=False)

        self._finalize()

    def _finalize(self):
        if self.all_dfs:
            master = pd.concat(self.all_dfs, ignore_index=True)
            master.to_csv(os.path.join(self.folder, "MASTER_DATA.csv"), index=False)
            print("\n--- AUDIT REPORT ---")
            for entry in self.audit_log:
                print(f"{entry['File']}: {entry['Status']}")

# --- SETUP ---
if __name__ == "__main__":
    CONFIG = {
        2019: [8, 9, 10, 11, 12], 2020: [8, 9, 10, 11],
        2021: [8, 9, 10, 11], 2022: [8, 9, 10, 11, 12],
        2023: [8, 9, 10, 11, 12, 13], 2024: [8, 9, 10, 11, 12]
    }
    PATTERN = r'(\d{2}/\d{2})\s+(.*?)\s+(\$?\d+[\d,]*\.\d{2})'
    
    proc = SavorProcessor(pattern=PATTERN, year_config=CONFIG)
    manager = BatchManager(folder="./statements", processor=proc)
    manager.run_pipeline()
