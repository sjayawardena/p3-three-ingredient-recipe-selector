import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p3-three-ingredient-recipe-selector')


def choose_recipe_type():
    """
    Get sweet or savoury recipe type choice from user.
    Use a while loop to validate whether user has entered "sweet" or "savoury"
    via the terminal.
    The user will be repeatedly prompted to enter their choice until valid.
    """
    while True:
        input_recipe_type_choice = input(
            'Please enter either "sweet" or "savoury": \n')
        recipe_type_choice = input_recipe_type_choice
        if validate_recipe_type_choice(recipe_type_choice):
            print(f"Thank you for choosing {recipe_type_choice}!")
            break
    return recipe_type_choice


def validate_recipe_type_choice(choice):
    """
    Return True if user entered "sweet" or "savoury".
    If not, then raise a value error, prompting them to try again.
    """
    if choice == "sweet" or choice == "savoury":
        return True
    try:
        if choice != "sweet" or choice != "savoury":
            raise ValueError(
                f'You entered "{choice}"'
            )
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        return False

def main():
    choose_recipe_type()

main()
