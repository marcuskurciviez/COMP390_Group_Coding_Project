import requests
from bs4 import BeautifulSoup

GET_REQUEST_HEADER = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                   'Safari/537.36',
     'Accept-Language': 'en-US, en;q=0.5'}
)


def find_base_url(keywords: str):
    base_url = 'https://www.amazon.com/s?k='
    search_keywords = keywords.replace(' ', '+')
    page_parameter = '&page=1'
    search_url = f'{base_url}{search_keywords}{page_parameter}'
    return search_url
    # print(search_url)


def get_search_results(s_url):
    # issue GET request
    response_obj = requests.get(s_url, headers=GET_REQUEST_HEADER)
    # print(response_obj.content)
    b_soup_obj = BeautifulSoup(response_obj.content, 'html.parser')
    # print(b_soup_obj)
    search_results = b_soup_obj.find_all('div', attrs={'class': 's-result-item', 'data-component-type': 's-search-result'})
    # print(type(search_results))
    # print(search_results[0])
    print(len(search_results))
    return search_results


def find_rating_results(s_url):
    num_rating = None
    first_result_product_rating = None
    first_result_product_title = None
    for result_item in s_url:
        first_result_product_title = result_item.h2.text
        # print(first_result_product_title)
        try:
            first_result_product_rating = result_item.find('i', attrs={'class': 'a-icon'})
            # print(first_result_product_rating.text)
            num_rating = result_item.find('span', {'class': 'a-size-base s-underline-text'})
            # print(num_rating.text)
        except AttributeError:
            print('No Product Rating')
    return first_result_product_title, first_result_product_rating.text, num_rating.text


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


def show_results():
    search_url = find_base_url('over ear headphones')
    search_results = get_search_results(search_url)
    for item in search_results:
        rating_data = find_rating_results(item)
        item_price = find_pricing_results(item)
        print(rating_data, item_price)
