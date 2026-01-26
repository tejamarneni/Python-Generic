import re
import os
import pdfplumber
import pandas as pd

def clean_pdf(path: str, year: int, target_pages: list, pattern: str) -> pd.DataFrame:
    # 1. Reset the list inside the function to avoid data duplication
    all_transactions = []
    
    with pdfplumber.open(path) as pdf:
        for p_idx in target_pages:
            try:
                page = pdf.pages[p_idx]
                words = page.extract_words()
                
                if not words: 
                    continue
                
                df_words = pd.DataFrame(words)
                page_lines = df_words.groupby("top")["text"].apply(lambda x: " ".join(x)).reset_index()
                
                for line in page_lines['text']:
                    matches = re.findall(pattern, line)
                    for m in matches:
                        all_transactions.append({
                            "Date": f"{m[0]}/{year}",
                            "Full_Description": m[1].strip(),
                            "Amount": m[2]
                        })
            except IndexError:
                print(f"Warning: Page index {p_idx} not found in {path}")

    df_final = pd.DataFrame(all_transactions)
    if df_final.empty: 
        return df_final

    # 2. Sequential Cleaning
    # Remove phone numbers first (often contain hyphens/spaces that confuse city splits)
    phone_pattern = r'\d{3}[-\s]\d{3}[-\s]\d{4}'
    df_final['Full_Description'] = df_final['Full_Description'].str.replace(phone_pattern, '', regex=True)

    df_final["Amount"] = df_final["Amount"].str.replace("$","",regex=False).apply(float)

    # Remove store numbers (#72) and long numeric IDs
    df_final['Full_Description'] = df_final['Full_Description'].str.replace(r'#\d+', '', regex=True)
    df_final['Full_Description'] = df_final['Full_Description'].str.replace(r'\d{3,}', '', regex=True)

    # 3. Robust State/City Extraction
    state_pattern = r'(.*)\s+([A-Z]{2})$'
    extracted = df_final['Full_Description'].str.extract(state_pattern)
    
    # Only update if the regex actually found a State
    df_final['State'] = extracted[1]
    # Keep original text if extraction failed (e.g., streaming services)
    df_final['Full_Description'] = extracted[0].fillna(df_final['Full_Description'])

    # 4. Final Polish
    df_final['Full_Description'] = df_final['Full_Description'].str.strip().str.title()
    
    return df_final.reset_index(drop=True)

# Define the path relative to the container's WORKDIR
data_folder = 'data'
pattern = r'(\d{2}/\d{2})\s+(.*?)\s+(-?\$\d+\.\d+)'
year_config = {
    2019: [8, 9, 10, 11, 12],
    2020: [8, 9, 10, 11],
    2021: [8, 9, 10, 11],
    2022: [8, 9, 10, 11, 12],
    2023: [8, 9, 10, 11, 12, 13],
    2024: [8, 9, 10, 11, 12],
    2025: [8, 9, 10, 11, 12]
}

for filename in os.listdir(data_folder):
    if filename.endswith(".pdf"):
        # Extract 4 digits from the filename to get the year
        year_match = re.search(r'(\d{4})', filename)
        if year_match:
            file_year = int(year_match.group(1))
            pages = year_config.get(file_year, [8, 9, 10, 11]) # Default if not in dict
            
            filepath = os.path.join(data_folder, filename)
            df = clean_pdf(path=filepath, year=file_year, target_pages=pages, pattern=pattern)
            
            output_path = os.path.join(data_folder, f'savor_{file_year}.csv')
            df.to_csv(output_path, index=False)
            print(f"Successfully processed {file_year}")
