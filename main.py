import db_funcs
import scrapper_funcs


def main():
    db_connection = db_funcs.establish_database_connection('amazon_db.db')
    db_cursor = db_funcs.create_db_cursor(db_connection)
    db_funcs.set_up_tables(db_cursor)

    search_terms = ['over ear headphones', 'usb microphones', '1080p webcams', 'capture_cards',
                    '8-channel audio mixers', 'gaming laptops']
    for term in search_terms:
        db_funcs.fill_tables(db_cursor, term)

    db_funcs.commit_and_close(db_connection, db_cursor)


if __name__ == '__main__':
    """ runs the main() function """
    main()

