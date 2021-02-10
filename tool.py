import pandas as pd 
import sys

excel_file = sys.argv[1]

data_xls = pd.read_excel(excel_file, dtype=str, index_col=None)
data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False, header=False)