import argparse
import os 
from helpfun import*

# parsing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file',
    help='filepath of excel, csv file file'
)
#todo create tex file as default location of tex table
parser.add_argument('-d','--destination',
    default=None,
    help='[optional]: destination of .tex file with table \nDefault: new table.tex file in same dir as excel file'
)
parser.add_argument('-s', '--sheet',
    default='Sheet1',
    help='[oprional]: sheet in excel file \nDefault: Sheet1'
)
parser.add_argument('-t', '--tabletypes',
    default=None,
    help='show all aviable types of latex tables'
)
parser.add_argument('-ct', '--choose_tabletypes',
    default=None,
    help='[optional]: choose within the aviable table types; to see them all please use -t or --tabletypes\n Default type 1'
)
args = parser.parse_args()

#save command line arguments in vars
given_file =  args.file
destination = args.destination
sheet = args.sheet
show_table_types = args.tabletypes
choosen_table_type = args.choose_tabletypes

#detrmine filetype, extracting path 
filename, file_extension = os.path.splitext(given_file)
table_file  = filepath(destination, filename, 0)
csv_file_path = filepath(destination, filename, 1)
if file_extension == '.csv' or file_extension == '.xlsx':
    if file_extension == '.xlsx':
        to_csv(given_file, csv_file_path, sheet)
        given_file = csv_file_path
    if choosen_table_type == '1':
        csvsimple(table_file, given_file)
    if choosen_table_type == '2':
        pandas(given_file, table_file)

    
else:
    raise Exception('file should be either an .csv or .xlsx file. Given was {}'.format(file_extension))



