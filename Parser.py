from bs4 import BeautifulSoup
import requests
import urllib3

def parser():
    urllib3.disable_warnings()
    url = 'https://www.omgtu.ru/ecab/persons/index.php?b=14'
    page = requests.get(url, verify=False)
    print(page.status_code)
    soup = BeautifulSoup(page.text,"html.parser")

    block=soup.findAll('div', class_='person__name')
    description = ''
    textfile = open('persons.txt', "w+", encoding="utf-8")
    for data in block:
        if data.find('a'):
            description = data.text
            print(description)
            textfile.write(description)

    textfile.close

