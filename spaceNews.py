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
    for i in range(0, 5):
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
    
    print(f'''
At the German research site, wissenschaft.de, the current topics are:\n{currentTopicName1}\n{linkOfTopic1}\n{currenttopicName2}\n{linkOfTopic2}
Other articles include:
''')
    for i in range(len(otherArticles5)):
        print(f'{otherArticles5[i][15:]}\n{otherArtcilesLinks5[i]}\n')

    
def shanghaiObservatory():
    url = 'https://english.shao.cas.cn/ne/rn/'
    response = requests.get(url)
    htmlContent = response.content
    soup = bs4.BeautifulSoup(htmlContent, "html.parser")
    articles = soup.select('.main .container .content-box .top-head-box .main-content .puti-box ul#content.tuwen-item li a[href]')
    
    #find the links and their coresponding titles
    listOfContent = []
    for a in articles:
        link = a.get("href", "")
        title = a.get("title", "")
        if link:
            link = "https://english.shao.cas.cn/ne/rn" + link[1:]
            listOfContent.append(title + "\n" + link + "\n")
    print(f'At the Chinese Astronomical Observatory, the newest articles include:\n')
    for i in range(5):
        print(f'{listOfContent[i]}')
        

def NAOJ ():
    url = 'https://www.nao.ac.jp/en/news/'
    response = requests.get(url)
    htmlContent = response.content
    soup = bs4.BeautifulSoup(htmlContent, "html.parser")
    
    articleClasses = soup.find_all(class_="l-column2-3__item")
    listOfContent = []
    for a in articleClasses:
        if str(a.find(class_="c-tag c-tag--ultramarine")) == '<span class="c-tag c-tag--ultramarine">Science</span>':
            polishedName = str(a.find(class_="c-heading4 c-card__heading c-card__heading--primary u-mt1"))[70:-5]
            tags = a.find_all('a')
            links = [tag['href'] for tag in tags]
            for i in links:
                i = "https://www.nao.ac.jp" + i
            listOfContent.append(polishedName + '\n' + i)
            
    print("And from The National Astronomical Observatory of Japan (NAOJ), the most recent 5 articles are:\n")
    for i in range(5):
        print(f'{listOfContent[i]}\n')






#TODO: repeat ths for at least 3-4 other sites
wissenSchaftDE()
shanghaiObservatory()
NAOJ()