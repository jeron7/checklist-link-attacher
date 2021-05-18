import requests
from bs4 import BeautifulSoup

def get_link_title(link):
    page = requests.get(link)
    title = ''
    if (page.status_code == 200):
        soup = BeautifulSoup(page.text, 'html.parser')
        og_title = soup.find("meta",  property="og:title");
        if (og_title == None):
            title = soup.find("title").getText()
        else:
            title = og_title.attrs['content']
    return title