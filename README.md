# Card-Management-Database
Database System utilizing .csv files and Python

The Card Management Database is a personal project that aims to provide a user-friendly and efficient way to manage cards for a game called Shadowverse: Evolved. 

Using python, the database allows for easy entry of new cards into a formatted Excel spreadsheet. Any new data entered using the program is automatically added to the associated .csv file for easy retrieval and organization.
Upon program launch, the database utilizes this .csv file to create a Pandas dataframe, providing convenient access to all the card information in a display.

  - The Card_Management_Program.py initializes the dataframe and main menu display. It also includes ensures that a clean file is being used in the current dataframe for display purposes. 

  - The Card_Database_Functions.py file contains the two main functions that are used in every iteration of the program running. One function is used to clean the selected .csv file and ensure that relevant data is being processed. And the other is used to update the database file, with the file of cleaned data. 

  - The Add_Card_Functions.py file is used only to add new card entries to the dataframe

  - The Card_Search_Functions.py file allows the user to search the dataframe for specific cards or card traits, and displays the results. This file also includes input validation and error messages for invalid entries. 

  - The Shadowverse Master List.csv is the original excel file that includes all of the card information. This file may contain errors or invalid formatting.

  - The Cleaned Shadowverse Master List.csv is the file that is updated in the main program, and contains the cleaned information that will be used in the dataframe display. 
