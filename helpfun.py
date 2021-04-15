import pandas as pd
import csv 

#get file path
def filepath(destination, filename, mode):
    if mode == 0:
        if destination != None:
            return destination
        else:
            x = filename.rfind('/')
            return filename[0:x] + '/table.tex'
    if mode == 1:
        x = filename.rfind('/')
        return filename[0:x] + '/csvfile.csv'
    else:
        print('fun didn\'t work this way')
        return -1

#tables
#csvsumple packag
def csvsimple(tex_file, csv_file):
    print('requierd: \\usepackage{csvautotabular}')
    f = open(tex_file, 'a')
    s = '\\csvautotabular{' + csv_file + '}'
    f.write(s)
    f.close()

#pandas to_latex
def pandas(csv_file, tex_file):
    print('requierd: \\usepackage{booktabs}')
    df = pd.read_csv(csv_file)
    df.to_latex(buf=tex_file)

#very basic
def basic(csv_file, tex_file):
    f = open(tex_file, 'a')
    f.write('\\begin{center}\n')
    cols = col_csv(csv_file)
    s = '\\begin{tabular}{'
    for i in range(cols):
        s += ' c'
    s += ' }\n'
    s2 = modify_line(csv_file)
    s3 = s + s2 + '\\end{tabular} \n\\end{center}' 
    f.write(s3)
    f.close()

#simple
def simple(csv_file, tex_file):
    f = open(tex_file, 'a')
    f.write('\\begin{center}\n\\begin{tabular}{ ')
    cols = col_csv(csv_file)
    s = ''
    for i in range(cols):
        s += '| c '
    s += '| }\n \\hline\n'
    s2 = modify_line(csv_file)
    s3 = s + s2 + '\\hline\n\\end{tabular}\n\\end{center}'
    f.write(s3)
    f.close()

#simple 2.0
def simple_2(csv_file, tex_file):
    f = open(tex_file, 'a')
    f.write('\\begin{center}\n\\begin{tabular}{ ')
    cols = col_csv(csv_file)
    s = ''
    for i in range(cols):
        s += '| c'
    s += '| }\n \\hline\n'
    s2 = modify_line(csv_file).replace('\n', '\n \\hline \n')
    s3 = s + s2 + '\\end{tabular}\n\\end{center}'
    f.write(s3)
    f.close()

#table for swe
def swe_table(csv_file, tex_file):
    f = open(tex_file, 'a')
    f.write('\\begin{table}\n\\centering\n\\tiny\n\\begin{tabularx}{\\textwidth}{')
    cols = col_csv(csv_file)
    s = ''
    for i in range(cols):
        s += '|l'
    s += '|} \n \\hline \n'
    s2 = modify_line(csv_file).replace('\n', '\n\\hline\n')
    s3 = s + s2 + '\\end{tabularx}\n\\end{center}'
    f.write(s3)
    f.close()

#other stuff
#convert to csv
def to_csv(excel_file, csv_file, sheet):
    data_xls = pd.read_excel(excel_file, sheet, dtype=str, index_col=None)
    data_xls.to_csv(csv_file, encoding='utf-8', index=False, header=False)

#count number of colums in .csv file
def col_csv(csv_file):
    f = open(csv_file, 'r')
    r = csv.reader(f, delimiter=',')
    r_value = len(next(r))
    f.close()
    return r_value

#modify lines of csv file to fit latex code
def modify_line(csv_file):
    f = open(csv_file, 'r')
    s = f.read().replace(',', ' & ').replace('\n',' \\\\ \n' )
    f.close()
    return s