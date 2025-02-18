import pandas as pd
from Card_Database_Functions import save_database_to_csv

#initialize existing dataframe for testing
#df = pd.read_csv("Shadowverse Master List.csv")

#add card functions
def add_card(df):
    
    #get new card information
    card_name = input("Enter card name: ")
    quantity = input("Enter card quantity: ")
    card_type = input("Enter card type (F=Follower, E=Evolved S=Spell, A=Amulet, T=Token, FE=Follower Evolved, FT=Follower Token, etc): ")
    rarity = input("Enter card rarity (0=Normal, *=Foil, *L=Foil Legendary, *SL=Foil Super Legendary, *PR=Foil Promo): ")
    
    #create new dictionary for the card to fit the dataframe row
    new_card = {
        "Card Name": card_name,
        "Quantity": quantity,
        "Type": card_type,
        "Rarity": rarity
        }
    
    #convert the new_card dictionary into a single row DataFrame
    new_card_df = pd.DataFrame([new_card])
    
    #add the new card dataframe to the existing dataframe
    df = pd.concat([df, new_card_df], ignore_index=True)
    
    print(f"\n\n{card_name} added to the database\n")
    save_database_to_csv(df)
    return df

#for testing
#add_card(df)
#print(df)