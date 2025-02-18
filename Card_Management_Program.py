import pandas as pd
from Card_Database_Functions import update_database_from_csv, save_database_to_csv, view_database, clean_csv
from Card_Search_Functions import card_search
from Add_Cards_Functions import add_card

# Set display options to show all columns and rows in a single block
pd.set_option("display.max_rows", 1000)       # Shows all rows without truncation
pd.set_option("display.max_columns", 500)    # Shows all columns without truncation
pd.set_option("display.width", None)          # Adjusts the display width to show all columns side-by-side
pd.set_option("display.colheader_justify", "center")  # Aligns column headers to the left for readability
pd.set_option("display.expand_frame_repr", False)   # Prevents line breaks within the DataFrame display

#validate and clean the csv file before using in the dataframe
clean_csv("Shadowverse Master List.csv", "Cleaned Shadowverse Master List.csv")

#initialize dataframe
df = pd.read_csv("Cleaned Shadowverse Master List.csv")

#main menu program
def main():
    global df
    
    #main menu
    while True:
        print("-" * 80)
        print("1) Search for cards")
        print("\n2) Add Cards")
        print("\n3) Update Database from modified csv file")
        print("\n4) Display Database")
        print("\n5) Exit")
        print("-" * 80)
    
        #get user menu choice
        choice = input("\nSelect an option 1-5: ")
        
        if choice == "1":
            card_search(df)
        elif choice == "2":
            df = add_card(df)
        elif choice == "3":
            df = update_database_from_csv()
        elif choice == "4":
            view_database(df)
        elif choice == "5":
            save_database_to_csv(df)
            print("\nExiting Program...")
            break
        else:
            print("\nInvalid Selection. Choose an option.")         
 
        
#Runs the main menu
if __name__ == "__main__":
    main()