import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok:  # 200 = true or other codes = false
        return r.text
    print(r.status_code)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='currencies').find('tbody').find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
    try:
        name = tds[1].find('a', class_='currency-name-container').text.strip()
    except:
        name = ''
    try:
        url = 'https://coinmarketcap.com/' + tds[1].find('a', class_='currency-name-container').get('href')
    except:
        url = ''
    try:
        price = tds[3].find('a').get('data-usd').strip()
    except:
        price = ''
    data = {'name': name,
            'url': url,
            'price': price}
    write_csv(data)


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data['name'], data['url'], data['price'])


def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
