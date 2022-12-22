import sqlite3
import db_funcs
import requests
from bs4 import BeautifulSoup

GET_REQUEST_HEADER = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                   'Safari/537.36',
     'Accept-Language': 'en-US, en;q=0.5'}
)


"""find_base_url serves the purpose of taking in a number of parameters and has the amazon base URL with the
beginning part, as well as a replace command to raplace spaces in the text with a + sign. As well as adds 
a page_parameter variable for each page number."""
def find_base_url(keywords: str, page_num: int):
    base_url = 'https://www.amazon.com/s?k='
    search_keywords = keywords.replace(' ', '+')
    page_parameter = '&page=' + str(page_num)
    search_url = f'{base_url}{search_keywords}{page_parameter}'
    return search_url
    # print(search_url)


"""Issues a GET request, using the html attributes."""
def get_search_results(s_url):
    # issue GET request
    response_obj = get_request(s_url)
    b_soup_obj = BeautifulSoup(response_obj.content, 'html.parser')
    # print(b_soup_obj)
    search_results = b_soup_obj.find_all('div',
                                         attrs={'class': 's-result-item', 'data-component-type': 's-search-result'})
    # print(type(search_results))
    # print(search_results[0])

    return search_results


"""Scrapper function to find the rating result from the Amazon webpage, uses a try/ except block for pulling the html
attributes from the page."""
def find_rating_results(s_url):
    num_rating = None
    first_result_product_rating = None
    first_result_product_title = None
    url = None
    for result_item in s_url:
        first_result_product_title = result_item.h2.text
        # print(first_result_product_title)
        try:
            first_result_product_rating = result_item.find('i', attrs={'class': 'a-icon'})
            # print(first_result_product_rating.text)
            num_rating = result_item.find('span', {'class': 'a-size-base s-underline-text'})
            # print(num_rating.text)
            url = 'https://www.amazon.com/' + result_item.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get('href')
        except AttributeError:
            print('No Product Rating')
    return first_result_product_title, first_result_product_rating.text, num_rating.text, url


def find_pricing_results(s_url):
    full_price = None
    for result_item in s_url:
        try:
            integer_price = result_item.find('span', {'class': 'a-price-whole'})
            cent_price = result_item.find('span', {'class': 'a-price-fraction'})
            full_price = integer_price.text + cent_price.text
            # print(full_price)
        except AttributeError:
            print('No Product Price')
    return full_price


def show_results_for_page(search_url: str):
    search_results = get_search_results(search_url)
    return search_results


"""attempts a GET request to the URL passed as a parameter, uses try/except block to catch errors
returns a response object if successful, otherwise returns None"""
def _safe_get_request(url: str):
    response = None
    try:
        response = requests.get(url, headers=GET_REQUEST_HEADER)
        print('GET request executed with no errors')
    except requests.exceptions.RequestException as request_exception:
        print(f'GET request failed with the following error: {request_exception}')
    finally:
        return response


"""attempts GET request on the URL passed as a parameter and reports status returns a response object"""
def get_request(url: str):
    response = _safe_get_request(url)
    if response is None:
        print(f'GET request error! No response object.')
        return None
    if response.status_code != 200:
        print(f'GET request error! {response.status_code} [{response.reason}]')
        return response
    else:
        print(f'GET request successful! {response.status_code} [{response.reason}]')
        return response


"""Extracts the product name and will return the name and print it to the database, if none is found then it will 
print an erorr message."""
def extract_product_name(listing):
    try:
        return find_rating_results(listing)[0]
    except AttributeError:
        print('No product name')


"""Extracts the product rating from the scrapper function find_rating_results. Will return the rating results, if none
is found then an error message will print."""
def extract_product_rating(listing):
    try:
        return find_rating_results(listing)[1][:3]
    except AttributeError:
        print('No product rating')


"""extracts the number of ratings for a listing, if none is found then no product ratings is outputted."""
def extract_num_ratings(listing):
    try:
        ratings = find_rating_results(listing)[2]
        if ratings[:1] == '(':
            return ratings[1:-1]
        else:
            return ratings
    except AttributeError:
        print('No product ratings')


"""Try except format for finding the pricing list results, if none is found then no product price is outputted into 
terminal."""
def extract_product_price(listing):
    try:
        return find_pricing_results(listing)
    except AttributeError:
        print('No product price')


"""Extracts the product URL in a try except layout, if no URL is found it will throw an error message."""
def extract_product_url(listing):
    try:
        return find_rating_results(listing)[3]
    except AttributeError:
        print('No product url')


"""Extracts the info from the several functions, and puts them in a variable for the database rows."""
def extract_info(listing):
    db_table_row_data = [None, None, None, None, None]
    db_table_row_data[0] = extract_product_name(listing)
    db_table_row_data[1] = extract_product_rating(listing)
    db_table_row_data[2] = extract_num_ratings(listing)
    db_table_row_data[3] = extract_product_price(listing)
    db_table_row_data[4] = extract_product_url(listing)
    return db_table_row_data
