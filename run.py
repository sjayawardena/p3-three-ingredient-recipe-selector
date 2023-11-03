import random
import time
import sys
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("p3-three-ingredient-recipe-selector")


def choose_recipe_type():
    """
    Get sweet or savoury recipe type choice from user.
    Use a while loop to validate whether user has entered "sweet" or "savoury"
    via the terminal.
    The user will be repeatedly prompted to enter their choice until valid.
    """
    print("Welcome to the Three-Ingredient Recipe Selector.\n")
    while True:
        input_recipe_type_choice = input(
            'Please enter either "sweet" or "savoury": \n'
        ).lower()
        recipe_type_choice = input_recipe_type_choice
        if validate_recipe_type_choice(recipe_type_choice):
            print(f"\nThank you for choosing {recipe_type_choice}!\n")
            break
    return recipe_type_choice


def validate_recipe_type_choice(choice):
    """
    Return True if user successfully entered "sweet" or "savoury".
    If not, then raise a value error, prompting them to try again.
    """
    if choice == "sweet" or choice == "savoury":
        return True
    try:
        if choice != "sweet" or choice != "savoury":
            raise ValueError(f'You entered "{choice}"')
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        return False


def sweet_or_savoury():
    """
    Give user a choice of sweet or savoury recipes.
    Run corresponding function for each choice.
    """
    chosen_recipe_type = choose_recipe_type()
    if chosen_recipe_type == "sweet":
        sweet_chosen()
    elif chosen_recipe_type == "savoury":
        savoury_chosen()


def sweet_chosen():
    """
    Randomly selects a recipe from the "sweet" worksheet of the
    linked Google Sheet.
    Includes 4-second time delays between 'fetching' message
    and recipe and steps appearing.
    """
    print("Fetching your randomly selected sweet recipe...\n")
    time.sleep(4)
    sweet_sheet = SHEET.worksheet("sweet")
    sweet_item = sweet_sheet.row_values(random.randint(2, 11))
    print(
        f"RECIPE: {sweet_item[0]}\n"
        + f"\nIndredient 1: {sweet_item[1]}\n"
        + f"Ingredient 2: {sweet_item[2]}\n"
        + f"Ingredient 3: {sweet_item[3]}\n"
        + f"\n30 minutes or under? {sweet_item[4]}\n"
    )
    print("\nFetching cooking steps...\n")
    time.sleep(4)
    print("\nSTEPS: \n" + f"\n{sweet_item[5]}")


def savoury_chosen():
    """
    Checks if user wants meat or no meat.
    Use a while loop to check if the user has successfully
    entered "meat" or "no meat" from the terminal.
    Then randomly selects a recipe from the "savoury, meat" or
    the "savoury, no meat" worksheet of the linked Google Sheet.
    Includes 4-second time delays between 'fetching' message
    and recipe and steps appearing.
    """
    while True:
        input_meat_or_not = input('Please enter either "meat" or "no meat": \n').lower()
        meat_or_not = input_meat_or_not
        if validate_meat_or_not(meat_or_not):
            print(f"\nThank you for choosing {meat_or_not}!\n")
            break
    if meat_or_not == "meat":
        print("Fetching your randomly selected savoury with meat recipe...\n")
        time.sleep(4)
        savoury_meat_sheet = SHEET.worksheet("savoury, meat")
        savoury_meat_item = savoury_meat_sheet.row_values(random.randint(2, 11))
        print(
            f"RECIPE: {savoury_meat_item[0]}\n"
            + f"\nIndredient 1: {savoury_meat_item[1]}\n"
            + f"Ingredient 2: {savoury_meat_item[2]}\n"
            + f"Ingredient 3: {savoury_meat_item[3]}\n"
            + f"\n30 minutes or under? {savoury_meat_item[4]}\n"
        )
        print("\nFetching cooking steps...\n")
        time.sleep(4)
        print("\nSTEPS: \n" + f"\n{savoury_meat_item[5]}")
    elif meat_or_not == "no meat":
        print("Fetching your randomly selected savoury without meat recipe...\n")
        time.sleep(4)
        savoury_no_meat_sheet = SHEET.worksheet("savoury, no meat")
        savoury_no_meat_item = savoury_no_meat_sheet.row_values(random.randint(2, 10))
        print(
            f"RECIPE: {savoury_no_meat_item[0]}\n"
            + f"\nIndredient 1: {savoury_no_meat_item[1]}\n"
            + f"Ingredient 2: {savoury_no_meat_item[2]}\n"
            + f"Ingredient 3: {savoury_no_meat_item[3]}\n"
            + f"\n30 minutes or under? {savoury_no_meat_item[4]}\n"
        )
        print("\nFetching cooking steps...\n")
        time.sleep(4)
        print(f"\nSTEPS: \n" f"\n{savoury_no_meat_item[5]}")


def validate_meat_or_not(choice):
    """
    Return True if user entered "meat" or "no meat".
    If not, then raise a value error, prompting them to try again.
    """
    if choice == "meat" or choice == "no meat":
        return True
    try:
        if choice != "meat" or choice != "no meat":
            raise ValueError(f'You entered "{choice}"')
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        return False


def happy_with_recipe():
    """
    Ask user whether happy with recipe choice.
    Use a while loop to validate whether user has entered "yes" or "no"
    via the terminal.
    The user will be repeatedly prompted to enter their choice until valid.
    If user successfully enters 'yes', show end message then sys.exit().
    If user successfully enters 'no', then run try_again().
    """
    while True:
        input_is_user_happy = input(
            "\nAre you happy with the recipe selected for you?"
            + '\nPlease enter "yes" or "no":\n'
        ).lower()
        is_user_happy = input_is_user_happy
        if validate_is_user_happy(is_user_happy):
            print(f"\nYou chose {is_user_happy}...\n")
            break
    if is_user_happy == "yes":
        print("\nGreat! Enjoy your dish! And come back soon.\n")
        sys.exit()
    elif is_user_happy == "no":
        try_again()


def try_again():
    """
    Offer user to start the process again if not happy with recipe.
    If yes, run main() function from start.
    If not, goodbye message and sys.exit().
    """
    while True:
        input_try_again = input(
            '\nWould you like to try again?\nPlease enter "yes" or "no".\n'
        ).lower()
        try_again = input_try_again
        if validate_try_again(try_again):
            print(f"\nYou chose {try_again}...\n")
            break
    if try_again == "yes":
        main()
    elif try_again == "no":
        print("\nSorry we couldn't help today. Please come back soon. Goodbye!\n")
        sys.exit()


def validate_is_user_happy(choice):
    """
    Return True if user entered "yes" or "no" in response to if they
    are happy with recipe.
    If not, then raise a value error, prompting them to try again.
    """
    if choice == "yes" or choice == "no":
        return True
    try:
        if choice != "yes" or choice != "no":
            raise ValueError(f'You entered "{choice}"')
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        return False


def validate_try_again(choice):
    """
    Return True if user entered "yes" or "no" in response to if they
    would like to try the recipe selector again.
    If not, then raise a value error, prompting them to try again.
    """
    if choice == "yes" or choice == "no":
        return True
    try:
        if choice != "yes" or choice != "no":
            raise ValueError(f'You entered "{choice}"')
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        return False


def main():
    """
    Run all main functions.
    """
    sweet_or_savoury()
    happy_with_recipe()


main()

# Examples of getting stuff from sheet
# sweet_sheet = SHEET.worksheet("sweet")
# sweet_item = sweet_sheet.row_values(random.randint(2, 3))
# print(sweet_item)
