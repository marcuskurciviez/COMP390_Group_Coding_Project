"""This module is responsible for the print statements"""
import math


def opening_statement():
    product_category = 0
    while True:
        try:
            product_category = int(input("Choose a product category: \n 1. Over Ear Headphones \n 2. USB Microphones \n 3. 1080p Webcams \n"
                                         "4. Capture Cards \n 5. 8-channel Audio Mixers 6. Gaming Laptops \n"))
        except ValueError:
            print("Please enter a valid number 1-6")
            continue
        if 1 <= product_category <= 6:
            target_star_review()
        else:
            print('Please enter a valid number 1-6')


def target_star_review():
    star_rev = 0
    while True:
        try:
            star_rev = float(input("Enter a target star review (ex. '4.5'): "))
        except ValueError:
            print("Please enter a target star review between 0.0 and 5.0")
        if 0.0 <= star_rev <= 5.0:
            target_reviews()
        else:
            print('Please enter a target star review between 0.0 and 5.0.')


def target_reviews():
    reviews = 0
    while True:
        try:
            reviews = int(input("Enter a target number of reviews (ex. (\'1000\'):"))
        except ValueError:
            print("You did not enter a number.")
            continue
        if 0 <= reviews <= math.inf:
            target_price()
        else:
            print('Please enter a positive number.')


def target_price():
    price = 0
    while True:
        try:
            price = float(input("Enter a target price (ex. \'59.99\'): "))
        except ValueError:
            print("You did not enter a price.")
            continue
        if 0 <= price <= math.inf:
            equality_operator()
        else:
            print('Please enter a target price.')


def equality_operator():
    operator_list = [">", "<", ">=", "<=", "="]
    operator = input("Choose an equality operator: ")
    if operator.lower() in operator_list:
        print("test")
    else:
        print("You did not enter a correct equality operator.")


def print_statements():
    print(opening_statement())

print(print_statements())
