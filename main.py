import sqlite3

import db_funcs
import print_funcs


"""The main function establishes a connection to the database, as well as create a cursor to creat and set
up the tables for each of the search terms. It goes through a for loop for each search term and fills the table
with the appropriate data. After fill is done it will commit and close the database connection."""
def main():
    db_connection = db_funcs.establish_database_connection('amazon_db.db')
    db_cursor = db_funcs.create_db_cursor(db_connection)
    db_funcs.set_up_tables(db_cursor)
    search_terms = ['over ear headphones', 'usb microphones', '1080p webcams', 'capture_cards',
                    '8-channel audio mixers', 'gaming laptops']
    for term in search_terms:
        db_funcs.fill_tables(db_cursor, term)
    query(db_cursor)
    db_funcs.commit_and_close(db_connection, db_cursor)


"""The query function is used for the terminal print statements if the user would like to execute another
query or not. If user says no then the program will exit and quit. """
def query(db_cursor: sqlite3.Cursor):
    cont = input('Would you like to execute a query (y/n):')
    while cont == 'y':
        user_input = get_input()
        db_funcs.query(db_cursor, user_input)
        cont = input('Would you like to execute a query (y/n):')
    if cont == 'n':
        print('Exiting program...')


"""The get_input function is connected to the print_funcs file where all the user 
input handling is going on. Stores each function into a variable to store user input."""
def get_input():
    category = print_funcs.opening_statement()
    target_star = print_funcs.target_star_review()
    target_star_eq = print_funcs.equality_operator()
    target_reviews = print_funcs.target_reviews()
    target_reviews_eq = print_funcs.equality_operator()
    target_price = print_funcs.target_price()
    target_price_eq = print_funcs.equality_operator()
    return print_funcs.print_statement(str(category), target_star_eq, target_star, target_reviews_eq, target_reviews,
                                       target_price_eq, target_price)


if __name__ == '__main__':
    """ runs the main() function """
    main()
