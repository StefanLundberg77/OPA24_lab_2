import pandas as pd

# reading & cleaning data function
def read_clean_data(excel_file, skip=0):

    # creates a dict with the sheets and their respective DataFrames
    dfs = pd.read_excel(excel_file, sheet_name=None, skiprows=skip)

    # creates a list of tuples with dfs dimensions of the first sheet
    size = dfs[list(dfs.keys())[0]].shape

    # identify sheets with different dimensions then the first sheet
    sheets_to_drop = [sheet_name for sheet_name, df in dfs.items() if df.shape != size]

    # loop the list
    for sheet in sheets_to_drop:
        
        # drop the wrong size sheet
        dfs.pop(sheet)
    
    # return the sheets with relevant data
    return dfs

if __name__ == "__main__":
    
    #for testing purpose 
    excel_file = "data/riket2023_åk9_np.xlsx"

    cleaned_dfs = read_clean_data(excel_file, skip=8)
    print(cleaned_dfs)