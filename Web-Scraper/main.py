from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


def run():
    url = str(input("Input an Url to a Web Page\n"))
    html = urlopen(url)

    soup = BeautifulSoup(html, 'lxml')
    type(soup)

    # title = soup.title
    # print(title)

    soup.find_all('a')
    all_links = soup.find_all("a")

    names = []

    for link in all_links:
        print(link.get("title"))
        names.append(link.get("title"))

    names = list(dict.fromkeys(names))

    print(names)

    with open('names.csv', 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(names)

    csvFile.close()


if __name__ == '__main__':
    run()
