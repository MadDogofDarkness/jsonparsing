from html.parser import HTMLParser
import requests

class Myparser(HTMLParser):

        def handle_starttag(self, tag, attrs):
                if tag == 'meta':
                        print(f"tag: {tag} : {attrs}")
                else:
                        pass

        def handle_endtag(self, tag):
                #print("end tag: ", tag)
                pass

        def handle_data(self, data):
                if self.get_starttag_text() == 'meta':
                        print(data)
                

def getmeta(htmlinput):
        parser = Myparser()
        parser.feed(htmlinput)
        print('success!')

def look(siteurl):
    page = requests.get(str(siteurl))
    print(page)
    return page.text

def save(data):
    f = open('results.txt', 'a')
    f.write('\r')
    f.write(str(data))
    f.close()
    return "success"

if __name__ == '__main__':
    url = input("input url: ")
    #getmeta(look(url))
    look(url)

