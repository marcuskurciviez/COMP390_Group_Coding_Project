"""This module is responsible for the print statements"""
import math


"""Serves as the opening statement where user can select a number from 1-6. It is formatted in a while loop where
if the user enters a number within range it will continue on, if not it will loop back to the product category
telling the user to enter a number between 1-6."""
def opening_statement():
    while True:
        try:
            product_category = int(input(
                "Choose a product category: \n 1. Over Ear Headphones \n 2. USB Microphones \n 3. 1080p Webcams \n"
                " 4. Capture Cards \n 5. 8-channel Audio Mixers \n 6. Gaming Laptops \n"))
        except ValueError:
            print("Please enter a valid number 1-6")
            continue
        if 1 <= product_category <= 6:
            print(product_category)
            return product_category
        else:
            print('Please enter a valid number 1-6')
            opening_statement()


"""Serves purpose for the target star review where user can enter a number from 0-5, and will retrieve an error
if number is bigger than 5 or less than 0."""
def target_star_review():
    while True:
        try:
            star_rev = float(input("Enter a target star review (ex. '4.5'): "))
        except ValueError:
            print("Please enter a target star review between 0.0 and 5.0")
            continue
        if 0.0 <= star_rev <= 5.0:
            print(star_rev)
            return star_rev
        else:
            print('Please enter a target star review between 0.0 and 5.0.')
            target_star_review()


"""User can enter a target number of reviews, since there really is no cap on a number of reviews, the function
uses .inf for an infinite number but no less than 0."""
def target_reviews():
    while True:
        try:
            reviews = int(input("Enter a target number of reviews (ex. (\'1000\'):"))
        except ValueError:
            print("You did not enter a number.")
            continue
        if 0 <= reviews <= math.inf:
            return reviews
        else:
            print('Please enter a positive number.')
            target_reviews()


"""Same with the function above, user can input a price point that has virtually no cap on the max number since
the price can range from 0 to a really high number."""
def target_price():
    while True:
        try:
            price = float(input("Enter a target price (ex. \'59.99\'): "))
        except ValueError:
            print("You did not enter a price.")
            continue
        if 0 <= price <= math.inf:
            return price
        else:
            print('Please enter a target price.')
            target_price()


"""This function has an operator_list with a list of the different operator, user can only input one of the listed
operators that are shown in the list. If not it will print an error message and loop back to the equality operator."""
def equality_operator():
    operator_list = [">", "<", ">=", "<=", "="]
    operator = input("Choose an equality operator (>, <, >=, <=, =): ")
    if operator.lower() in operator_list:
        return operator
    else:
        print("You did not enter a correct equality operator.")
        equality_operator()


"""Openinging print statement that takes in a number of parameters for each user input. After all is done, it will
return a SQL select statement that will be used for filtering the data."""
def print_statement(category, eq1, targ_star, eq2, targ_rev, eq3, targ_price):
    table_name_dict = {
        "1": "Over_Ear_Headphones",
        "2": "USB_Microphones",
        "3": "Webcams",
        "4": "CaptureCards",
        "5": "Audio_Mixers",
        "6": "Gaming_Laptops"
    }
    return("SELECT * FROM " + table_name_dict[category] + " WHERE rating " + eq1 + " " + str(
        targ_star) + " AND num_ratings " + eq2 + " " + str(targ_rev) + " AND price " + eq3 + " " + str(targ_price))
