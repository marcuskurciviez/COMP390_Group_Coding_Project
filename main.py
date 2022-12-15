import scrapper_funcs
import db_funcs


def main():
    db_connection = db_funcs.establish_database_connection('amazon_db.db')
    db_cursor = db_funcs.create_db_cursor(db_connection)
    db_funcs.set_up_tables(db_cursor)

    search_url = scrapper_funcs.find_base_url('over ear headphones')
    # print(search_url)
    search_results = scrapper_funcs.get_search_results(search_url)
    # print(search_results)
    scrapper_funcs.find_rating_results(search_results)
    scrapper_funcs.find_pricing_results(search_results)

    db_cursor.execute('''INSERT INTO Over_Ear_Headphones VALUES(?, ?, ?, ?, ?)''',
                      ('Headphones', 4.5, 10000, 19.99, 'https://www.amazon.com/'))

    db_funcs.commit_and_close(db_connection, db_cursor)


if __name__ == '__main__':
    """ runs the main() function """
    main()
