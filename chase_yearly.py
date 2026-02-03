import os
import re
import pandas as pd
import pdfplumber

path = '/Users/dummypath/SpendingReportChase.pdf'
pattern = r"([A-Z][a-z]{2}\s\d{2},\s\d{4})\s+([A-Z][a-z]{2}\s\d{2},\s\d{4})(.*?)\s+(-?\$\d+\.\d+)"
regex_pattern = re.compile(pattern)
target_pages = [0,1]
all_transactions = []

with pdfplumber.open(path) as pdf:
    for page in target_pages:
        pages = pdf.pages[page]
        words = pages.extract_words()
        df_words = pd.DataFrame(words)
        page_lines = df_words.groupby("top")["text"].apply(lambda x: " ".join(x)).reset_index()
        for line in page_lines['text']:
            matches = regex_pattern.findall(line)
            for m in matches:
                all_transactions.append({
                            "TransactionDate": m[0],
                            "PostedDate": m[1],
                            "Full_Description": m[2].strip(),
                            "Amount": m[3]
                        })
                      
df = pd.DataFrame(all_transactions)
df[["TransactionDate","PostedDate"]] = df[["TransactionDate","PostedDate"]].apply(pd.to_datetime,format="%b %d, %Y")
df["Amount"] = df["Amount"].str.replace('$','',regex=False).apply(float)
df
