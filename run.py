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
    print(f"The data that provided is {data_str}")

get_sales_data()
