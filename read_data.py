import pandas as pd
from pathlib import Path # we import a clas called path from lib pathlib


def read_data():
    data_path = Path(__file__).parents[0]/"data"#\resultat-ansokningsomgang-2024.xlsx"]
    df = pd.read_excel(data_path/"resultat-ansokningsomgang-2024.xlsx", skiprows=5, sheet_name="Tabell 3")
    return df



if __name__ == "__main__":
    #testing purpose
    #print(data_path)
    df = read_data()
    print(df.columns)
    




# pd.set_option('future.no_silent_downcasting', True)

# # reading & cleaning data function
# def read_cleaned_data(excel_file, skip=0):

#     # creates a dict with the sheets and their respective DataFrames
#     dfs = pd.read_excel(excel_file, sheet_name=None, skiprows=skip)

#     # creates a list of tuples with dfs dimensions of the first sheet
#     size = dfs[list(dfs.keys())[0]].shape

#     # loop through and identify sheets with different dimensions then the first sheet
#     sheets_to_drop = [sheet_name for sheet_name, df in dfs.items() if df.shape != size]

#     # sheet 1 as reference sheet
#     ref_sheet = dfs[list(dfs.keys())[0]]

#     for sheet, df in dfs.items():
        
#         # Loopa genom referensens kolumner
#         for col in ref_sheet.columns:  

#             # Kontrollera att kolumnen finns i det aktuella bladet
#             if col in df.columns:  
                
#                 df[col] = df[col].replace({"..": 0, "~100": 100}, regex=False)
                
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
#                   "Totalt\n (A-F)",
#                   "Flickor\n (A-F)",
#                   "Pojkar\n (A-F)",
#                   "Totalt\n (A-E)",
#                   "Flickor\n (A-E)",
#                   "Pojkar\n (A-E)",
#                   "Totalt\n (poäng)",
#                   "Flickor\n (poäng)",
#                   "Pojkar\n (poäng)"]

# # function for renaming columns
# def rename_columns(dfs):
        
#         # iterate through dfs and change column names to match layout
#         for sheet, df in dfs.items():
#             df.columns = [column_names]
#             return dfs

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
# #for testing purpose 
# if __name__ == "__main__":
    
#     # file variable
#     excel_file = "data/riket2023_åk9_np.xlsx"

#     # the returned cleaned file
#     cleaned_dfs = read_cleaned_data(excel_file, skip=8)
#     print(cleaned_dfs)