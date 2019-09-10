import requests
from bs4 import BeautifulSoup
import csv


# get HTML source code from url
def get_html(url):
    r = requests.get(url)
    return r.text


# function to write into CSV file
def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'],
                         data['symbol'],
                         data['url'],
                         data['price']])  # choose rows to write into csv


# main function to get data from site
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', id='currencies').find('tbody').find_all('tr')  # find all rows in table
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[1].find('a', class_='currency-name-container').text
        symbol = tds[1].find('a').text
        url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')  # create valid url from paths
        price = tds[3].find('a').get('data-usd')
        data = {'name': name,
                'symbol': symbol,
                'url': url,
                'price': price}  # create data structure to write into csv
        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'  # source of data
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
