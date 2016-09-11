"""
Web grabber
"""

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
import json


def get_stock_page(symbol):
    """Gets url for stock page."""
    return 'https://finance.yahoo.com/quote/PBR-A?p={0}'.format(symbol)


def my_function_01():
    # url = 'http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts'
    r = urllib.urlopen(get_stock_page('PBR-A')).read()
    soup = BeautifulSoup(r, "lxml")
    print(type(soup))
    print(soup.prettify()[0:5000])


def my_function_02():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Firefox()
    url = get_stock_page('PBR-A')
    driver.get(url)
    driver.implicitly_wait(10)
    print(driver.page_source)
    # assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()

    # elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def my_function_03():
    import requests
    url = ('http://finance.yahoo.com/webservice/v1/symbols/'
           'allcurrencies/quote?format=json')
    r = requests.get(url)
    print(r.status_code)
    # verify is ok value = 200 if not write error message.

    print(r.text)
    my_json = r.json()
    #  print(json.dumps(my_json))

    # Get the quote for brazilian real in dollars
    # "name": "USD/BRL",
    for element in my_json['list']['resources']:
        print(json.dumps(element))
        print('\n')


def main():
    #  my_function_01()
    my_function_03()

if __name__ == '__main__':
    main()
