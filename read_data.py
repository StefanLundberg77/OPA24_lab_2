import pandas as pd

# reading & cleaning data function
def read_excel_data(excel_file):
    df = pd.read_excel(excel_file)
    return df

if __name__ == "__main__":
    #for testing purpose 
    excel_file = "data/riket2023_åk9_np.xlsx"
    df = read_excel_data(excel_file)
    print(df)