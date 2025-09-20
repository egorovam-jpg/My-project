import pandas as pd
FILE_ID = "1M1-EG2MXn_kv-A-sVe50zwn7D6csOfF1"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"
raw_data = pd.read_csv(file_url)
print(raw_data.head(10))