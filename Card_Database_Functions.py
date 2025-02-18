import pandas as pd

#uncomment for testing
#df = pd.read_csv("Shadowverse Master List.csv")

def clean_csv(input_file="Shadowverse Master List.csv", output_file="Cleaned Shadowverse Master List.csv"):
    try:
        df = pd.read_csv(input_file)
        
        #check all of these columns in the dataframe
        check_columns = ["Card Name", "Quantity", "Type", "Rarity"]
        
        # Convert the relevant columns to strings to ensure no integer zeros
        df[check_columns] = df[check_columns].astype(str)
    
        #checks that all of the columns read zero is True, then flips the boolean with the ~ operator
        #only removes rows where all specified columns are zero or empty
        cleaned_df = df[~(df[check_columns] == "0").all(axis=1)]
    
        #update csv file to be used in the dataframe
        cleaned_df.to_csv(output_file, index=False)
        print(f"\nCSV file cleaned and saved to {output_file}.")
    except FileNotFoundError:
        print(f"File {input_file} not found. Verify file location.")
    except Exception as e:
        print(f"An error has occurred: {e}")

def update_database_from_csv(file_path="Cleaned Shadowverse Master List.csv"):
    try:
        df = pd.read_csv(file_path)
        print("\n\nDatabase updated from the cleaned csv file.\n")
    except FileNotFoundError:
        print("\nCSV file not found. Verify file path.")
    return df

def save_database_to_csv(df, file_path="Cleaned Shadowverse Master List.csv"):
    df.to_csv(file_path, index=False)
    print("\nDatabase saved to the cleaned CSV file.")
    

#uses panda display options to control the rows/columns displayed
def view_database(df):
    print(df)
    
#for testing
#update_database(df)
#save_database(df)
#view_database(df)
#clean_csv()