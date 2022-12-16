""" This module assists with functions relating to the database"""
import sqlite3


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


def create_headphones_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Over_Ear_Headphones(
                                           product_name TEXT,
                                           rating REAL,
                                           num_ratings INTEGER,
                                           price REAL,
                                           product_url TEXT);''')


def create_microphones_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS USB_Microphones(
                                            product_name TEXT,
                                            rating REAL,
                                            num_ratings INTEGER,
                                            price REAL,
                                            product_url TEXT);''')


def create_webcams_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Webcams(
                                            product_name TEXT,
                                            rating REAL,
                                            num_ratings INTEGER,
                                            price REAL,
                                            product_url TEXT);''')


def create_capture_cards_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Capture_Cards(
                                           product_name TEXT,
                                           rating REAL,
                                           num_ratings INTEGER,
                                           price REAL,
                                           product_url TEXT);''')


def create_audio_mixers_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Audio_Mixers(
                                            product_name TEXT,
                                            rating REAL,
                                            num_ratings INTEGER,
                                            price REAL,
                                            product_url TEXT);''')


def create_gaming_laptops_table(db_cursor: sqlite3.Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Gaming_Laptops(
                                                   product_name TEXT,
                                                   rating REAL,
                                                   num_ratings INTEGER,
                                                   price REAL,
                                                   product_url TEXT);''')


def clear_tables(db_cursor: sqlite3.Cursor):
    # clear the tables if it already has data from the last time the program was run
    db_cursor.execute('DELETE FROM Over_Ear_Headphones')
    db_cursor.execute('DELETE FROM USB_Microphones')
    db_cursor.execute('DELETE FROM Webcams')
    db_cursor.execute('DELETE FROM Capture_Cards')
    db_cursor.execute('DELETE FROM Audio_Mixers')
    db_cursor.execute('DELETE FROM Gaming_Laptops')


def set_up_tables(db_cursor: sqlite3.Cursor):
    """ creates the tables we will put our products into, or if the table exists deletes current values"""
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


def commit_and_close(db_connection: sqlite3.Connection, db_cursor: sqlite3.Cursor):
    """commits, changes, and closes the connection/cursor"""
    try:
        db_connection.commit()
        db_cursor.close()
        db_connection.close()
        print('Changes committed and connection/cursor closed successfully, program finished!')
    except sqlite3.Error as db_error:
        print(f'An error occurred while committing connection and closing cursor: {db_error}')