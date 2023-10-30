import random
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
            print(f"Thank you for choosing {recipe_type_choice}!\n")
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


def sweet_or_savoury():
    chosen_recipe_type = choose_recipe_type()
    if chosen_recipe_type == "sweet":
        print(sweet_chosen())
    elif chosen_recipe_type == "savoury":
        print(savoury_chosen())


def sweet_chosen():
    """
    Randomly selects a recipe from the 
    "sweet" worksheet of the linked Google Sheet.
    """
    print("Here is your randomly selected sweet recipe...\n")
    sweet_sheet = SHEET.worksheet("sweet")
    # Update last number in range as list grows
    sweet_item = sweet_sheet.row_values(random.randint(2, 3))
    return sweet_item


def savoury_chosen():
    """
    Checks if user wants meat or no meat.
    Use a while loop to check if the user has entered "meat"
    or "no meat" from the terminal.
    Then randomly selects a recipe from the "savoury, meat" or 
    the "savoury, no meat" worksheet of the linked Google Sheet.
    """
    while True:
        input_meat_or_not = input(
            'Please enter either "meat" or "no meat": \n')
        meat_or_not = input_meat_or_not
        if validate_meat_or_not(meat_or_not):
            print(f"Thank you for choosing {meat_or_not}!\n")
            break
    if meat_or_not == "meat":
        print("Here is your randomly selected savoury with meat recipe...\n")
        savoury_meat_sheet = SHEET.worksheet("savoury, meat")
        # Update last number in range as list grows
        savoury_meat_item = savoury_meat_sheet.row_values(random.randint(2, 3))
        return savoury_meat_item
    elif meat_or_not == "no meat":
        print("Here is your randomly selected savoury without meat recipe...\n")
        savoury_no_meat_sheet = SHEET.worksheet("savoury, no meat")
        # Update last number in range as list grows
        savoury_no_meat_item = savoury_no_meat_sheet.row_values(
            random.randint(2, 3))
        return savoury_no_meat_item


def validate_meat_or_not(choice):
    """
    Return True if user entered "meat" or "no meat".
    If not, then raise a value error, prompting them to try again.
    """
    if choice == "meat" or choice == "no meat":
        return True
    try:
        if choice != "meat" or choice != "no meat":
            raise ValueError(
                f'You entered "{choice}"'
            )
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        return False


def main():
    """
    Run all main functions.
    """
    sweet_or_savoury()


main()

# Examples of getting stuff from sheet
# sweet_sheet = SHEET.worksheet("sweet")
# sweet_item = sweet_sheet.row_values(random.randint(2, 3))
# print(sweet_item)
