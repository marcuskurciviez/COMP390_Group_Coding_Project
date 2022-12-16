import scrapper_funcs
import db_funcs


def simple_print():
    # Testing purposes only
    print("Potato")


def main():
    db_connection = db_funcs.establish_database_connection('amazon_db.db')
    db_cursor = db_funcs.create_db_cursor(db_connection)
    db_funcs.set_up_tables(db_cursor)

    result_list = scrapper_funcs.show_results()
    print(f'{result_list} test variable')

    db_cursor.execute('''INSERT INTO Over_Ear_Headphones VALUES(?, ?, ?, ?, ?)''',
                      ('Headphones', 4.5, 10000, 19.99, 'https://www.amazon.com/'))

    db_funcs.commit_and_close(db_connection, db_cursor)


if __name__ == '__main__':
    """ runs the main() function """
    main()
