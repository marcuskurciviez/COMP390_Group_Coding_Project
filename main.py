import scrapper_funcs

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    search_url = scrapper_funcs.find_base_url('headphones')
    # print(search_url)
    search_results = scrapper_funcs.get_search_results(search_url)
    # print(search_results)
    scrapper_funcs.find_rating_results(search_results)
    scrapper_funcs.find_pricing_results(search_results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
