import re
import os
import pdfplumber
import pandas as pd

class SavorProcessor:
    def __init__(self, pattern: str, year_config: dict):
        self.pattern = pattern
        self.year_config = year_config
        # Regex attributes for internal cleaning
        self.phone_pattern = r'\d{3}[-\s]\d{3}[-\s]\d{4}'
        self.junk_pattern = r'#\d+|\d{3,}'
        self.state_pattern = r'(.*)\s+([A-Z]{2})$'

    def _extract_raw_data(self, path: str, year: int, pages: list) -> pd.DataFrame:
        """Extracts text lines from specific PDF pages based on year config."""
        all_transactions = []
        try:
            with pdfplumber.open(path) as pdf:
                for p_idx in pages:
                    if p_idx >= len(pdf.pages):
                        continue
                        
                    page = pdf.pages[p_idx]
                    words = page.extract_words()
                    if not words: continue
                        
                    df_words = pd.DataFrame(words)
                    page_lines = df_words.groupby("top")["text"].apply(lambda x: " ".join(x))
                    
                    for line in page_lines:
                        matches = re.findall(self.pattern, line)
                        for m in matches:
                            all_transactions.append({
                                "Source_File": os.path.basename(path),
                                "Date": f"{m[0]}/{year}",
                                "Full_Description": m[1].strip(),
                                "Amount": m[2]
                            })
        except Exception as e:
            print(f"  ! Error reading {path}: {e}")
            
        return pd.DataFrame(all_transactions)

    def _clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Polishes the raw data into a usable format."""
        if df.empty: return df

        # 1. Currency to Float
        df["Amount"] = df["Amount"].str.replace("$", "", regex=False).apply(float)

        # 2. Description Scrubbing
        df['Full_Description'] = (df['Full_Description']
                                  .str.replace(self.phone_pattern, '', regex=True)
                                  .str.replace(self.junk_pattern, '', regex=True))

        # 3. State/City Logic
        extracted = df['Full_Description'].str.extract(self.state_pattern)
        df['State'] = extracted[1]
        df['Full_Description'] = extracted[0].fillna(df['Full_Description'])

        # 4. Final Formatting
        df['Full_Description'] = df['Full_Description'].str.strip().str.title()
        return df.reset_index(drop=True)

    def process_single_file(self, filepath: str, year: int) -> pd.DataFrame:
        """Public method to run the pipeline for one file."""
        pages = self.year_config.get(year, [8, 9, 10, 11])
        raw_df = self._extract_raw_data(filepath, year, pages)
        return self._clean_dataframe(raw_df)


class BatchManager:
    def __init__(self, data_folder: str, processor: SavorProcessor):
        self.data_folder = data_folder
        self.processor = processor
        self.processed_dfs = [] # Storage for consolidation

    def run(self):
        """Processes all PDFs in the folder."""
        for filename in os.listdir(self.data_folder):
            if not filename.lower().endswith(".pdf"):
                continue

            year_match = re.search(r'(\d{4})', filename)
            if not year_match: continue

            file_year = int(year_match.group(1))
            filepath = os.path.join(self.data_folder, filename)
            
            print(f"Processing: {filename}...")
            df = self.processor.process_single_file(filepath, file_year)
            
            if not df.empty:
                self.processed_dfs.append(df)
                output_path = os.path.join(self.data_folder, f'savor_{file_year}.csv')
                df.to_csv(output_path, index=False)
        
        self.compile_master_report()

    def compile_master_report(self):
        """Combines all individual years into one master CSV."""
        if not self.processed_dfs:
            print("No data to compile.")
            return

        master_df = pd.concat(self.processed_dfs, ignore_index=True)
        master_path = os.path.join(self.data_folder, "MASTER_TRANSACTIONS.csv")
        master_df.to_csv(master_path, index=False)
        print(f"\n--- SUCCESS ---")
        print(f"Master file created at: {master_path}")
        print(f"Total Transactions Processed: {len(master_df)}")

# --- START SCRIPT ---
if __name__ == "__main__":
    # 1. Data Config
    PATTERN = r'(\d{2}/\d{2})\s+(.*?)\s+(\$?\d+\.\d{2})'
    YEAR_PAGES = {
        2019: [8, 9, 10, 11, 12], 2020: [8, 9, 10, 11],
        2021: [8, 9, 10, 11], 2022: [8, 9, 10, 11, 12],
        2023: [8, 9, 10, 11, 12, 13], 2024: [8, 9, 10, 11, 12],
        2025: [8, 9, 10, 11, 12]
    }
    FOLDER_PATH = "./my_statements" # Update this to your path

    # 2. Initialize and Run
    savor_tool = SavorProcessor(pattern=PATTERN, year_config=YEAR_PAGES)
    manager = BatchManager(data_folder=FOLDER_PATH, processor=savor_tool)
    manager.run()
