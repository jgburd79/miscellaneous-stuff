import pdfplumber
import pandas as pd
import os
from regs import clean_row_single


def pdf_tables_to_dataframe(pdf):
    """Extract all tables from each page
       and put in a list of pandas dataframes called dataframes_list"""
    with pdfplumber.open(pdf) as pdf:
        
        dataframes_list = []
        
        for page in pdf.pages:
            
            for table in page.extract_tables():
                temp = []
                for row in table:
                    
                    # The clean_row_single function is used to format each row
                    # taking care of inconsistent column entries
                    # such as where patterns like ['1 of 1F'] appear where
                    # this should be separated as in ['1 of 1', 'F']
                    # or ['of 1'] should appear as in ['1 of 1'].
                    # None or "" whitespace values are also filtered out
                    # to ensure that the columns align correctly.
                    temp.append(clean_row_single(row))
                
                table = temp
                
                df = pd.DataFrame(table)
                
                dataframes_list.append(df)
        
        return dataframes_list


def multiple_dfs(df_list, file_name, spaces):
    
    # Creating Excel Writer Object from Pandas
    
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
   
    row = 0
    for dataframe in df_list:
        dataframe.to_excel(writer, sheet_name='Tables', startrow=row, startcol=0, index=False, header=False)
        row = row + len(dataframe.index) + spaces + 1
    writer.save()

    os.system(file_name)
