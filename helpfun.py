import pandas as pd

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


#convert to csv
def to_csv(excel_file, csv_file, sheet):
    data_xls = pd.read_excel(excel_file, sheet, dtype=str, index_col=None)
    data_xls.to_csv(csv_file, encoding='utf-8', index=False, header=False)