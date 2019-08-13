from lxml import html
import requests

def look(siteurl):
    page = requests.get(str(siteurl))
    tree = html.fromstring(page.content)
    print(tree)
    results = []
    return page.text

def save(data):
    f = open('results.txt', 'a')
    f.write('\r')
    f.write(str(data))
    f.close()
    return "success"

if __name__ == '__main__':
    url = input("input url: ")
    print(save(look(url)))
