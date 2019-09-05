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
    elem = soup.find_all('article', class_='course')
    for e in elem:
        try:
            name = e.find('h3').text
        except:
            name = ''
        try:
            duration = e.find('div', class_='course-duration').find('span').text
        except:
            duration = ''
        try:
            course_status = e.find('div', class_='course-status').text
        except:
            course_status = ''
        data = {'name': name,
                'duration': duration,
                'course_status': course_status}
        write_csv(data)


def write_csv(data):
    with open('courses.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['duration'],
                         data['course_status']))


def main():
    pattern = 'https://coursehunter.net/backend/python?page={}'
    for i in range(1, 5):
        url = pattern.format(i)
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()
