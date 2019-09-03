import requests
from bs4 import BeautifulSoup
import csv


# get HTML source code from url
def get_html(url):
    r = requests.get(url)
    return r.text


# function to write into CSV file
def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))


# normalize price separator
def refined(s):
    r = s.split(' ')[0]
    return r.replace(',', '')


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    featured = soup.find_all('section')[1]
    plugins = featured.find_all('article')
    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(r)
        data = {'name': name,
                'url': url,
                'reviews': rating}  # create data structure to write into csv
        write_csv(data)
    return len(plugins)


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
