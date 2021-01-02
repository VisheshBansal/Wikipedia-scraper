from bs4 import BeautifulSoup
import requests
from .section import Section
import re

def scrapWikipediaPage(topicname):
    ''' Extracts the web page page and converts to beautiful soup format , if an error occurs returns a -1'''
    try:
        page = requests.get("https://en.wikipedia.org/wiki/" + topicname)
    except:
        return -1
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        content = soup.select('div.mw-parser-output')[0]
        wikipagesection = organise(topicname, content)

        def crawler(page):
            '''crawls the urls present on the website'''
            re = requests.get('{}'.format(page))
            bs = BeautifulSoup(re.text.encode('utf-8'), "html.parser")
            with open("urlinks.txt", 'w+', encoding="utf-8") as url_links:
                for link in bs.find_all('a'):
                    if link.has_attr('href'):
                        url_links.writelines("{}\n".format(link.attrs['href']))
        return wikipagesection
    else:
        return -1


def organise(topic, soup):
    ''' Organises the texts into section objects .Each subsection is determined by heading type at the beginning'''
    WikiSection = Section(topic, "", 1)
    CurrentSection = WikiSection
    for element in soup:

        if element.name == "p" and element.text != None:
            CurrentSection.addText(element.text)

        elif element.name != None and element.name[0] == 'h':
            headinglevel = int(element.name[1])

            if headinglevel > CurrentSection.headinglevel:
                NewSection = Section(element.find('span').text, CurrentSection, headinglevel)
                CurrentSection.addSection(NewSection)
                CurrentSection = NewSection

            elif headinglevel <= CurrentSection.headinglevel:
                while CurrentSection.headinglevel != headinglevel:
                    CurrentSection = CurrentSection.parent
                NewSection = Section(element.find('span').text, CurrentSection.parent, CurrentSection.headinglevel)
                CurrentSection.parent.addSection(NewSection)
                CurrentSection = NewSection

    return WikiSection


