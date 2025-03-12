import pandas as pd

# reading & cleaning data function
def read_cleaned_data(excel_file, skip=0):

    # creates a dict with the sheets and their respective DataFrames
    dfs = pd.read_excel(excel_file, sheet_name=None, skiprows=skip)

    # creates a list of tuples with dfs dimensions of the first sheet
    size = dfs[list(dfs.keys())[0]].shape

    # loop through and identify sheets with different dimensions then the first sheet
    sheets_to_drop = [sheet_name for sheet_name, df in dfs.items() if df.shape != size]

    # loop the list
    for sheet in sheets_to_drop:
        
        # drop the wrong size sheet
        dfs.pop(sheet)

    dfs = rename_columns(dfs)

    # return the sheets with relevant data
    return dfs


column_names = ["Plats",  
                  "Huvudman",
                  "Totalt\n (A-F)",
                  "Flickor\n (A-F)",
                  "Pojkar\n (A-F)",
                  "Totalt\n (A-E)",
                  "Flickor\n (A-E)",
                  "Pojkar\n (A-E)",
                  "Totalt\n (poäng)",
                  "Flickor\n (poäng)",
                  "Pojkar\n (poäng)"]

# function for renaming columns
def rename_columns(dfs):
        
        # iterate through dfs and change column names to match layout
        for sheet, df in dfs.items():
            df.columns = [column_names]
            return dfs
        
#for testing purpose 
if __name__ == "__main__":
    
    # file variable
    excel_file = "data/riket2023_åk9_np.xlsx"

    # the returned cleaned file
    cleaned_dfs = read_cleaned_data(excel_file, skip=8)
    print(cleaned_dfs)