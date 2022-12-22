""" This module assists with functions relating to the database"""
import sqlite3
import scrapper_funcs


"""Establish_database_connection provides the necessary information to set up a connection with the
database in a try except format. If database fails to establish then an error message will occur. 
If successful then it will print out the appropriate statement for a successful connection."""
def establish_database_connection(db_name: str):
    """ attempts to establish a connection to the database, returns connection object or None if unsuccessful """
    db_connection = None
    try:
        db_connection = sqlite3.connect(db_name)
        print(f'Connection to database {db_name} established. DB connection: {db_connection}')
    except sqlite3.Error as db_error:
        print(f'An error occurred while trying to establish a connection to {db_name}: {db_error}')
    finally:
        return db_connection


"""create_db_cursor serves the purpose of making the database cursor object. It is in the format of a
try except where it will print a successful message if successful, or an error message if not successful."""
def create_db_cursor(db_connection: sqlite3.Connection):
    """creates a cursor object on the database from the given connection. Returns the cursor, or None if not created"""
    db_cursor = None
    if db_connection is None:
        print('Cursor object not created, no connection object!')
        return None
    try:
        db_cursor = db_connection.cursor()
        print(f'Cursor object {db_cursor} created on {db_connection}')
    except sqlite3.Error as db_error:
        print(f'An error occurred while trying to create cursor object: {db_error}')
    finally:
        return db_cursor


"""This table has the purpose of creating the table for the headphones table. Goes through the execute command
and will create a table if it does not exist already with the appropriate values of product_name, rating,
num_ratings, price, and product URL."""
def create_headphones_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Over_Ear_Headphones(
                                           product_name TEXT,
                                           rating REAL,
                                           num_ratings INTEGER,
                                           price REAL,
                                           product_url TEXT);''')


"""This table has the purpose of creating the table for the microphones table. Goes through the execute command
and will create a table if it does not exist already with the appropriate values of product_name, rating,
num_ratings, price, and product URL."""
def create_microphones_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS USB_Microphones(
                                            product_name TEXT,
                                            rating REAL,
                                            num_ratings INTEGER,
                                            price REAL,
                                            product_url TEXT);''')


"""This table has the purpose of creating the table for the webcams table. Goes through the execute command
and will create a table if it does not exist already with the appropriate values of product_name, rating,
num_ratings, price, and product URL."""
def create_webcams_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Webcams(
                                            product_name TEXT,
                                            rating REAL,
                                            num_ratings INTEGER,
                                            price REAL,
                                            product_url TEXT);''')


"""This table has the purpose of creating the table for the capture cards table. Goes through the execute command
and will create a table if it does not exist already with the appropriate values of product_name, rating,
num_ratings, price, and product URL."""
def create_capture_cards_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Capture_Cards(
                                           product_name TEXT,
                                           rating REAL,
                                           num_ratings INTEGER,
                                           price REAL,
                                           product_url TEXT);''')


"""This table has the purpose of creating the table for the audio mixers table. Goes through the execute command
and will create a table if it does not exist already with the appropriate values of product_name, rating,
num_ratings, price, and product URL."""
def create_audio_mixers_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Audio_Mixers(
                                            product_name TEXT,
                                            rating REAL,
                                            num_ratings INTEGER,
                                            price REAL,
                                            product_url TEXT);''')


"""This table has the purpose of creating the table for the gaming laptops table. Goes through the execute command
and will create a table if it does not exist already with the appropriate values of product_name, rating,
num_ratings, price, and product URL."""
def create_gaming_laptops_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Gaming_Laptops(
                                                   product_name TEXT,
                                                   rating REAL,
                                                   num_ratings INTEGER,
                                                   price REAL,
                                                   product_url TEXT);''')


"""The purpose for this function is to delete the data from the tables listed above, if the data is already 
inserted into the program from the last time is was ran."""
def clear_tables(db_cursor: sqlite3.Cursor):
    # clear the tables if it already has data from the last time the program was run
    db_cursor.execute('DELETE FROM Over_Ear_Headphones')
    db_cursor.execute('DELETE FROM USB_Microphones')
    db_cursor.execute('DELETE FROM Webcams')
    db_cursor.execute('DELETE FROM Capture_Cards')
    db_cursor.execute('DELETE FROM Audio_Mixers')
    db_cursor.execute('DELETE FROM Gaming_Laptops')


""" creates the tables we will put our products into, or if the table exists deletes current values"""
def set_up_tables(db_cursor: sqlite3.Cursor):
    try:
        create_headphones_table(db_cursor)
        create_microphones_table(db_cursor)
        create_webcams_table(db_cursor)
        create_capture_cards_table(db_cursor)
        create_audio_mixers_table(db_cursor)
        create_gaming_laptops_table(db_cursor)
        clear_tables(db_cursor)
        print('Tables set up successfully')
    except sqlite3.Error as db_error:
        print(f'An error occurred while trying to set up tables: {db_error}')


    """commits, changes, and closes the connection/cursor"""
def commit_and_close(db_connection: sqlite3.Connection, db_cursor: sqlite3.Cursor):
    try:
        db_connection.commit()
        db_cursor.close()
        db_connection.close()
        print('Changes committed and connection/cursor closed successfully, program finished!')
    except sqlite3.Error as db_error:
        print(f'An error occurred while committing connection and closing cursor: {db_error}')


def insert_values_into_table(db_cursor: sqlite3.Cursor, search_term: str, data: tuple):
    if search_term == '1080p webcams':
        table_name = 'webcams'
    elif search_term == '8-channel audio mixers':
        table_name = 'Audio_Mixers'
    else:
        table_name = search_term.replace(' ', '_')
    db_cursor.execute(f'''INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?)''',
                      (data[0], data[1], data[2], data[3], data[4]))


def fill_tables(db_cursor: sqlite3.Cursor, search_term: str):
    counter = 0
    page = 1
    while counter < 300:
        url = scrapper_funcs.find_base_url(search_term, page)
        search_results = scrapper_funcs.show_results_for_page(url)
        for item in search_results:
            counter += 1
            if counter > 300:
                break
            db_table_row_data = scrapper_funcs.extract_info(item)
            insert_values_into_table(db_cursor, search_term, tuple(db_table_row_data))
        page += 1


"""The query function serves the purpose of creating a text document with the results from the database 
with the user filtering and printing it to the created document."""
def query(db_cursor: sqlite3.Cursor, query_str):
    f = open("results.txt", "w")
    f.write(query_str)
    print(query_str)
    db_cursor.execute(f'''{query_str}''')
    output = db_cursor.fetchall()
    for item in output:
        print(item)
        print("")
        f.write(f"\n{item}")
    f.close()

