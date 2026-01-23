import pdfplumber
import pandas as pd
import re

def clean_statement_data(df):
    # 1. Standardize to Title Case for better visuals
    df['Description'] = df['Description'].str.title()
    
    # 2. Remove Store Numbers and jammed-together locations
    # Matches patterns like 'Store 09315Richmondva' or '034782Midlothianva'
    df['Description'] = df['Description'].str.replace(r'Store \d+\S+', '', regex=True)
    df['Description'] = df['Description'].str.replace(r'\d{5,}\S+', '', regex=True)
    
    # 3. Fix Duplicated Names (e.g., 'Netflix.Comnetflix.Comca')
    # We look for common streaming patterns and shorten them
    df['Description'] = df['Description'].str.replace(r'Netflix.*', 'Netflix', regex=True)
    df['Description'] = df['Description'].str.replace(r'Disney Plus.*', 'Disney+', regex=True)
    
    # 4. Clean up Delivery Services (e.g., 'Uber *Eats...')
    df['Description'] = df['Description'].str.replace(r'Uber\s*\*?Eats.*', 'Uber Eats', regex=True)
    
    # 5. Final Trim
    df['Description'] = df['Description'].str.strip()
    
    return df

# 1. Load the PDF
pdf_path = "/Users/dummypath/dummy.pdf"
pattern = r"(\w{3} \d+)\s+(\w{3} \d+)\s+(.*?)\s+\$([\d.]+)"

with pdfplumber.open(pdf_path) as pdf:
    # Target Page 3 (index 2) [cite: 128]
    page = pdf.pages[2] 
    
    # 2. Extract Table
    # pdfplumber finds the table boundaries automatically
    table = page.extract_table()

# 3. Find the text pattern and get the cleaned format using regex
pattern = r"(\w{3} \d+)\s+(\w{3} \d+)\s+(.*?)\s+\$([\d.]+)"
matches = re.findall(pattern=pattern,string=table[2][0])

# 4. Load into Pandas
df = pd.DataFrame(matches[1:], columns=["Transaction_Date","Posted_Date","Description","Amount"])

# 5. Initial Cleanup
# Removing the '$' and converting Amount to numeric for analysis
df['Amount'] = df['Amount'].str.replace('$', '').str.replace(',', '').astype(float)

df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'] + ' 2025', format='%b %d %Y')
df['Posted_Date'] = pd.to_datetime(df['Posted_Date'] + ' 2025', format='%b %d %Y')

# Apply the cleaning
df_final = clean_statement_data(df)
print(df_final)
