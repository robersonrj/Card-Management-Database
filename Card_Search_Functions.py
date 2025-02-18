import pandas as pd

#initialize existing dataframe for testing
#df = pd.read_csv("Shadowverse Master List.csv")

#card search functions menu
def card_search(df):
    while True:
        print("-" * 80)
        print("Search by:")
        print("\n1) Card Name")
        print("\n2) Quantity")
        print("\n3) Card Type")
        print("\n4) Card Rarity")
        print("\n5) Back")
        print("-" * 80)
        
        choice = input("\nSelect an option 1-5: ")
        
        #search by name
        if choice == "1":
            searched_card = input("What is the name of the card? ")
            #check if the searched_card is in the dataframe
            search_results = df[df["Card Name"].str.contains(searched_card, case=False, na=False)]
            
            if search_results.empty:
                print(f"\nNo card found with the name {searched_card}")
            else:
                print(search_results)            
        
        #search by quantity
        elif choice == "2":
            try:
                searched_quantity = int(input("What quantity of a card are you looking for? "))
                search_results = df[df.Quantity == searched_quantity]
                if search_results.empty:
                    print(f"\nNo card found with quantity {searched_quantity}")
                else:
                    print(search_results)  
            except ValueError:
                print("\nError. Enter a number value for the quantity.")
        
        #search by card type
        elif choice == "3":
            searched_type = input("What is the type of the card?\nF for Follower, S for Spell, A for Amulet, T for Token, or any combination of those:\n")
            #check if the searched_card is in the dataframe
            search_results = df[df["Type"].str.contains(searched_type, case=False, na=False)]
            
            if search_results.empty:
                print(f"\nNo card found with the type {searched_type}")
            else:
                print(search_results)    
        
        #search by rarity         
        elif choice == "4":
            searched_rarity = input("What is the rarity of the card?\n0 = Normal, * = Foil, *L = Foil Legendary, *SL = Foil Super Legendary, PR = Promo:\n")
            #check if the searched_card is in the dataframe
            search_results = df[df["Rarity"].str.contains(searched_rarity, case=False, na=False, regex=False)]
            
            if search_results.empty:
                print(f"\nNo card found with a rarity of {searched_rarity}")
            else:
                print(search_results)    
        
        elif choice == "5":
            #return to main()
            return
        
        else:
            print("\n\nInvalid selection. Choose an option.")
         
            
#for testing         
#card_search(df)