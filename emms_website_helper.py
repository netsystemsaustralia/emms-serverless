import requests
from bs4 import BeautifulSoup as bs
import re

class EmmsWebsiteHelper:

    def __init__(self):
        self.soup = ''
        self.base_url = 'http://www.nemweb.com.au'

    def getPage(self, url):
        #try:
            r = requests.get(url)
            self.soup = bs(r.content, "html.parser")
        #except expression as identifier:
            #pass

    def getLinks(self):
        links = []
        i = 0
        for link in self.soup.find_all('a', attrs={'href': re.compile(r"^/REPORTS/.+\.zip")}):
            #print(link.get('href'))
            #print(link.text)
            links.append({'name': link.text, 'href': '%s%s' % (self.base_url, link.get('href'))})
            if i == 5000:
                break
            i = i + 1
        return links

    def downloadFile(self, url, saveTo):
        r = requests.get(url)
        with open(saveTo, 'wb') as f:  
            f.write(r.content)

if __name__ == '__main__':
    h = EmmsWebsiteHelper()
    h.getPage("http://www.nemweb.com.au/REPORTS/CURRENT/DispatchIS_Reports/")
    l = h.getLinks()
    for link in l:
        print(link)
        h.downloadFile(link['href'], '%s%s' % ('./downloads/', link['name']))