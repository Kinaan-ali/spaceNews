import requests
import bs4



def wissenSchaftDE():
    url = "https://wissenschaft.de/astronomie-physik"
    response = requests.get(url)
    htmlContent = response.content
    soup = bs4.BeautifulSoup(htmlContent, "html.parser")

    currentTopics = soup.select('section.module[aria-label*="Aktuelle Astronomie"] .container .grid-2col article.card.card-lg a.card-link')
    linksCurrentTopics = soup.select('section.module[aria-label*="Aktuelle Astronomie"] .container .grid-2col article.card.card-lg a.card-link')

    listOfCurrentTopics = list(currentTopics)
    topic1 = str(listOfCurrentTopics[0])
    topic2 = str(listOfCurrentTopics[1])

    
    linkOfTopic1 = findLink(topic1)
    linkOfTopic2 = findLink(topic2)
    currentTopicName1 = findName(topic1)
    currenttopicName2 = findName(topic2)
    return f'Current topics:\n{currentTopicName1}\n{currenttopicName2}\nand their links: {linkOfTopic1}, {linkOfTopic2}'

def findName(name):
    split = name.split('"')
    nameOfTopic = split[1]
    finalName = nameOfTopic[15:]
    return finalName
def findLink(name):
    split = name.split('"')
    linkOfTopic = split[5]
    link = "https://wissenschaft.de" + linkOfTopic
    return link


print(wissenSchaftDE())
