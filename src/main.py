from googlesearch import search
from bs4 import BeautifulSoup
import requests

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
headers = {"User-Agent": user_agent}

def get_links(url):
    global headers
    text_block = "\n\n### "+ url.find("title").text +" ###"
    print(url.find("title").text)
    if "CNN" in url.find("title").text:
        url_links = url.find_all("a", recursive=True, class_="home__list__tag")
        for link in url_links:
            print(link.get("href"))
            myreq = requests.get(link.get("href"), headers=headers)
            url_text = BeautifulSoup(myreq.text, "html.parser")
            text_block += "\n"+url_text.text.strip()
            #print(url_text.text.strip())
    elif "Exame" in url.find("title").text:
        url_links = url.find_all("a", recursive=True, class_="touch-area")
        for link in url_links:
            if 'https://' in link.get('href'):
                print(link.get("href"))
                myreq = requests.get(link.get("href"), headers=headers)
            else:
                print("https://exame.com"+link.get("href"))
                myreq = requests.get("https://exame.com"+link.get("href"), headers=headers)
            url_text = BeautifulSoup(myreq.text, "html.parser")
            text_block += "\n"+url_text.text.strip()
            #print(url_text.text.strip())
    elif "Estadão" in url.find("title").text:
        url_links = url.find_all("a", recursive=True, class_="image")
        url_links += url.find_all("a", recursive=True, class_="news-link news-link-image")
        for link in url_links:
            print(link.get("href"))
            myreq = requests.get(link.get("href"), headers=headers)
            url_text = BeautifulSoup(myreq.text, "html.parser")
            text_block += "\n"+url_text.text.strip()
            #print(url_text.text.strip())
    elif "- União Química" in url.find("title").text:
        url_links = url.find_all("a", recursive=True, class_="botf")
        if len(url_links) == 0:
            text_block += "\n"+url.text.strip()
        for link in url_links:
            print(link.get("href"))
            myreq = requests.get(link.get("href"), headers=headers)
            url_text = BeautifulSoup(myreq.text, "html.parser")
            text_block += "\n"+url_text.text.strip()
            #print(url_text.text.strip())
    return text_block

mytext_block = ""
for link in search('"união química" notícias', stop=6):
    myreq = requests.get(link, headers=headers)
    print(link)
    print(myreq)
    #print(myreq.text)
    mytext_block += get_links(BeautifulSoup(myreq.text, "html.parser"))
mytext_block = mytext_block.replace("Continua após a publicidade", '')
print(mytext_block)
print("\n### Fim ###")