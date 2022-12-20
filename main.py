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


def y():
    search_results = scrapper_funcs.show_results_for_page('https://www.amazon.com/s?k=over+ear+headphones&page=1')
    for item in search_results:
        print("Name: " + str(scrapper_funcs.find_rating_results(item)[0]))
        print("Rating: " + str(scrapper_funcs.find_rating_results(item)[1]))
        print("Reviews: " + str(scrapper_funcs.find_rating_results(item)[2]))
        print("URL: " + str(scrapper_funcs.find_rating_results(item)[3]))
        print("Price: " + str(scrapper_funcs.find_pricing_results(item)))
        print('***********')


if __name__ == '__main__':
    """ runs the main() function """
    main()
    #y()
