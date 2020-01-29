from bs4 import BeautifulSoup
import re

# .find() find first usage of class or tag
# .find_all() find all usages
#
# .parent() find parent container for selected class or tag
# find_parent(class_='row') specify parent for selected obj
# .find_next_sibling() find next obj on the same level


def get_copywriter(tag):
    whois = tag.find('div', id='whois').taxt.strip()
    if 'Copywriter' in whois:
        return tag
    return None


def get_salary(s):
    pattern = r'\d{1, 9}'
    salary = re.findall(pattern, s)
    return salary


def main():
    file = open('index.html').read()

    soup = BeautifulSoup(file, 'lxml')
    #  FIND ALL ROWS
    row = soup.find_all('div', class_='row')
    # FIND DIV WITH ALENA in name
    alena = soup.find('div', text='Alena').parent
    # FIND ALL COPYWRITERS
    copywriters = []
    persons = soup.find_all('div', class_='row')
    for person in persons:
        cw = get_copywriter(person)
        if cw:
            copywriters.append(cw)
    # FIND SALARY FIELD
    salary = soup.find_all('div', {'data-set': 'salary'})
    for i in salary:
        print(get_salary(i.text))


if __name__ == '__main__':
    main()
