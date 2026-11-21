import requests
import bs4
import re



def wissenSchaftDE():
    def findName(name):
            split = name.split('"')
            nameOfTopic = split[1]
            finalName = nameOfTopic[15:]
            return finalName
    def findLink(name):
        #starts with ' href=" ' so have to give it an if statement because the one under else is out of range because of different extraction methods"
        if name.startswith("href="):
            linkOfTopic = name[6:]
            link = "https://wissenschaft.de" + linkOfTopic
            return link
        else:
            split = name.split('"')
            linkOfTopic = split[5]
            link = "https://wissenschaft.de" + linkOfTopic
            return link
    url = "https://wissenschaft.de/astronomie-physik"
    response = requests.get(url)
    htmlContent = response.content
    soup = bs4.BeautifulSoup(htmlContent, "html.parser")
    #find all the names of the Other Articles
    pattern = re.compile(r'"(Artikel[^"]*)"', re.IGNORECASE)
    #find all the links of the Other Articles
    linkPattern = re.compile(r'(href="[^"]*)"', re.IGNORECASE)
    

    currentTopics = soup.select('section.module[aria-label*="Aktuelle Astronomie"] .container .grid-2col article.card.card-lg a.card-link')
    linksCurrentTopics = soup.select('section.module[aria-label*="Aktuelle Astronomie"] .container .grid-2col article.card.card-lg a.card-link')
    weitereArtikelSoup = soup.select('section.module[aria-label*="Weitere Artikel"] .container .module-topics .article-list .card.card-md a.card-link')
    #get the first 5 articles and their links
    listOfOtherArticles = pattern.findall(str(weitereArtikelSoup))
    LinksOtherArticles = linkPattern.findall(str(weitereArtikelSoup))
    otherArticles5 = []
    otherArtcilesLinks5 = []
    i = 0
    #limit to 5 articles
    for i in range(1, 6):
        otherArticles5.append(listOfOtherArticles[i])
        i += 1

    #limit to 5 links, and join to make an absolute path link
    for i in range(1, 6):
        full = findLink(LinksOtherArticles[i])
        otherArtcilesLinks5.append(full)
        i +=1
  

   

    listOfCurrentTopics = list(currentTopics)
    topic1 = str(listOfCurrentTopics[0])
    topic2 = str(listOfCurrentTopics[1])

    
    linkOfTopic1 = findLink(topic1)
    linkOfTopic2 = findLink(topic2)
    currentTopicName1 = findName(topic1)
    currenttopicName2 = findName(topic2)
    return f'Current topics:\n{currentTopicName1}\n{currenttopicName2}\nand their links: {linkOfTopic1}, {linkOfTopic2}\nExtraTopics: {otherArticles5} and links: {otherArtcilesLinks5}'

    


print(wissenSchaftDE())


#TODO: repeat ths for at least 3-4 other sites
