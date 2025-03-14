import pandas as pd

# reading data function
def read_data(excel_file, sheets_to_read, columns, skip=0):

    # Data cleaning    
    
    # read excel file and create dicts of the sheets and merge them into a dataframe with new column with sheet names as column values
    df_merged = pd.concat(
    [pd.read_excel(excel_file, sheet_name=sheet, skiprows=skip, index_col=None).assign(Sheet=sheet)
    for sheet in sheets_to_read],
    ignore_index=True)

    # rename columns to new names
    df_merged.columns = columns

    # create a reference dataframe of sheet "Engelska"
    ref_sheet = df_merged[df_merged['sheet']=='Engelska']

    # create a copy of dataframe
    df_clean = df_merged.copy()

    # method to convert specific elements in df
    df_clean = df_clean.map(lambda x: 0 if x == ".." else (0 if x == "~100" else x))

    # method to convert column data type in dataframe to ref_sheet data types
    df_clean = df_clean.astype(ref_sheet.dtypes.to_dict(), errors="ignore")                          
    
    # save clean dataframe to df
    df = df_clean

    # return converted and cleaned dataframe            
    return df

# function for selecting sheet and cleaning
def sheet_filter(df, sheet_name):
    
    # create df with the selected sheet name
    df_sheet = df[df["sheet"] == sheet_name]#df.query("sheet == 'sheet_name'")

    # 
    df_clean_sheet = df_sheet.drop(columns=["sheet"]).reset_index(drop=True)

    return df_clean_sheet

def read_data_2(excel_file2, sheets_to_read, cols, skip=0, row=0):

    df = pd.read_excel(excel_file2, sheets_to_read, skiprows = skip, nrows = row,  usecols = cols)

    df.set_index('Unnamed: 0', inplace=True)

    df.index.names = ['Läsår']

    return df

#for testing purpose 
if __name__ == "__main__":
    
    # file variable
    excel_file = "data/riket2023_åk9_np.xlsx"

    # the returned cleaned file
    cleaned_df = read_data_2(excel_file, 8)

    # test print
    print(cleaned_df)

    # rename df
    df = cleaned_df
    
    # test function
    svenska = sheet_filter(df, "Matematik")
    
    # test print
    print("test",svenska)


# ----------------------------------------------------------------------------
# Old func    
# def read_data(excel_file, skip=0):
    
#     # data cleaning
#     # creates a dict with the sheets and their respective DataFrames
#     dfs = pd.read_excel(excel_file, sheet_name=None, skiprows=skip)

#     # creates a list of tuples with dfs dimensions of the first sheet
#     size = dfs[list(dfs.keys())[0]].shape

#     # loop through and identify sheets with different dimensions then the first sheet
#     sheets_to_drop = [sheet_name for sheet_name, df in dfs.items() if df.shape != size]

#     # sheet 1 as reference sheet
#     ref_sheet = dfs[list(dfs.keys())[0]]

#     # loop through dicts and their dataframes
#     for sheet, df in dfs.items():
        
#         # Loopa genom referensens kolumner
#         for col in ref_sheet.columns:  

#             # Kontrollera att kolumnen finns i det aktuella bladet
#             if col in df.columns:  
                
#                 df[col] = df[col].map(lambda x: 0 if x == ".." else (100 if x == "~100" else x))
                
#                 try:
#                     if ref_sheet.dtypes[col] in [int, float]:
#                         df[col] = pd.to_numeric(df[col], errors="coerce")
#                     else:
#                         df[col] = df[col].astype(ref_sheet.dtypes[col], errors="ignore")
#                 except FutureWarning:
#                     raise
                        
   
#     # loop the list and drop unwanted sheet
#     dfs = {sheet: df for sheet, df in dfs.items() if sheet not in sheets_to_drop}

#     # rename columns by function
#     dfs = rename_columns(dfs)
    
#     # return the sheets with relevant data
#     return dfs

# # list of names for layout
# column_names = ["Plats",  
#                   "Huvudman",
#                   "Totalt (A-F)",
#                   "Flickor (A-F)",
#                   "Pojkar (A-F)",
#                   "Totalt (A-E)",
#                   "Flickor (A-E)",
#                   "Pojkar(A-E)",
#                   "Totalt (poäng)",
#                   "Flickor (poäng)",
#                   "Pojkar (poäng)"]

# def convert_data(dfs):

#     # create a ref_sheet
#     ref_sheet = dfs[list(dfs.keys())[0]]

#     for sheet, df in dfs.items():
        
#         for col in ref_sheet.columns:  # Loopa genom referensens kolumner

#             if col in df.columns:  # Kontrollera att kolumnen finns i det aktuella bladet
                
#                 df[col] = df[col].replace({"..": 0, "~100": 100}, regex=False)  # Ersätt värden först

                
#                 if ref_sheet.dtypes[col] in [int, float]:
#                     df[col] = pd.to_numeric(df[col], errors="coerce")
#                 else:
#                     df[col] = df[col].astype(ref_sheet.dtypes[col], errors="ignore")
#     return dfs
# function for renaming columns in dict
# def rename_columns(dfs):
        
#         # iterate through dfs and change column names to match layout
#         for sheet, df in dfs.items():
#             df.columns = [column_names]
#             return dfs