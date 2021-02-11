import pandas as pd 
import argparse
from helpfun import*

# parsing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file',
    help='filepath of excel file'
)
#todo create tex file as default location of tex table
parser.add_argument('-d','--destination',
    default=None,
    help='[optional]: destination of .tex file with table \nDefault: new .txt file in same dir as excel file'
)
parser.add_argument('-s', '--sheet',
    default='Sheet 1',
    help='[oprional]: sheet in excel file \nDefault: Sheet 1'
)
parser.add_argument('-t', '--tabletypes',
    default=None
    help='show all aviable types of latex tables'
)
parser.add_argument('-ct', '--choose_tabletypes',
    default=None,
    help='[optional]: choose within the aviable table types; to see them all please use -t or --tabletypes\n Default type 1'
)
args = parser.parse_args()

#save command line arguments in vars
excel_file =  args.file
destination = args.destination
sheet = args.sheet
show_table_types = args.tabletypes
choosen_table_type = args.choose_tabletypes


# excel to csv
# data_xls = pd.read_excel(excel_file, dtype=str, index_col=None)
# data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False, header=False)