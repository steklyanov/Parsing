import requests
from bs4 import BeautifulSoup
import csv
import re
import vimeo_dl as vimeo
import urllib.request


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # body = soup.find('body')
    print(type(soup))
    day_counter = 0
    bodies = soup.find_all("body")
    for body in bodies:
        print(day_counter + 1)
        video_fames = body.find_all('iframe')
        lesson_counter = 0
        for frame in video_fames:
            m = re.search('src="(.+?)"', str(frame)).group(1)
            print(m)
            lesson_counter += 1
        day_counter += 1


def get_html():
    with open('qqq') as data:
        file = data.read()
        return file


def main():
    # url = 'https://marathon.miyabi.academy/#/user_marathon_day_exercise/d964879f-3c81-47fe-8bc2-7c0bdd5423d1/9aed7378-930a-4aa1-ac62-00dc7b891c8c'
    # data = get_html()
    # print(data)
    url = 'https://player.vimeo.com/video/323505617'
    # video = vimeo.new(url)
    # best = video.getbest()
    # best.download(quiet=False)
    urllib.request.urlretrieve(url, 'video_name.mp4')
    get_page_data(get_html())


if __name__ == '__main__':
    main()
