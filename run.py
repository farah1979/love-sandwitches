import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
     Get the request sales data from our users
    """
    print("Please enter the sales data from the last market")
    print("Data should be sex numbers saperated by commas")
    print("Example: 10, 5, 8, 23, 12, 9\n")
    data_str = input("Enter your data here: ")
    sales_data = data_str.split(",")
    validate_data(sales_data)
    

def validate_data(values):
    """
    Check if the user enter sex integer values
    """
    try: 
        [int (value) for value in values]
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values requierd, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data {e}. Please try again.\n")
    
    



get_sales_data()
