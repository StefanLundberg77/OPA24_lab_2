import pandas as pd

# function to read and clean data from file
def read_data(excel_file, sheets_to_read, columns, skip=0):   
    
    # Read specified sheets and merge them into a DataFrame
    df_merged = pd.concat(
    [pd.read_excel(excel_file, sheet_name=sheet, skiprows=skip, index_col=None).assign(Sheet=sheet)
    for sheet in sheets_to_read],
    ignore_index=True)

    # rename columns by list
    df_merged.columns = columns

    # create a reference dataframe of sheet "Engelska"
    ref_sheet = df_merged[df_merged['sheet']=='Engelska']

    # create a copy of dataframe
    df_clean = df_merged.copy()

    # replace ".." and "~100" with 0 in whole df
    df_clean = df_clean.map(lambda x: 0 if x == ".." else (0 if x == "~100" else x)) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html

    # convert column data types in dataframe to ref_sheet data types
    df_clean = df_clean.astype(ref_sheet.dtypes.to_dict(), errors="ignore")                          
    
    # save clean dataframe to df
    df = df_clean

    # return converted and cleaned dataframe            
    return df

# function for selecting sheet and cleaning
def sheet_filter(df, sheet_name):
    
    # create df with the selected sheet name
    df_sheet = df[df["sheet"] == sheet_name] # df.query("sheet == 'sheet_name'")

    # drop column sheet for layout purpose
    df_clean_sheet = df_sheet.drop(columns=["sheet"]).reset_index(drop=True)

    return df_clean_sheet

# read specific part of file
def read_data_2(excel_file2, sheets_to_read, cols, skip=0, row=0):

    # create dataframe from file + read specific sheets + skip rows for column names + select rows 
    df = pd.read_excel(excel_file2, sheets_to_read, skiprows = skip, nrows = row,  usecols = cols)

    # set the first column as index + rename to läsår
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