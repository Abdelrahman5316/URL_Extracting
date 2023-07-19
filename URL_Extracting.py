import requests
from bs4 import BeautifulSoup

def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    urls = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and ('http' in href or 'www' in href):
            urls.add(href)
            if 'curlie.org' in href or 'wikipedia.org' in href:
                urls.update(get_urls(href))
    return urls

if __name__ == '__main__':
    urls = get_urls('https://www.curlie.org/')
    print('Curlie URLs:')
    print('\n'.join(urls))
    urls = get_urls('https://www.wikipedia.org/')
    print('Wikipedia URLs:')
    print('\n'.join(urls))
