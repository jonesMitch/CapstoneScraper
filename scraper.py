from bs4 import BeautifulSoup as bs
import requests

url = "https://ndawn.info/snow_photos.html"
stakes = []

def scrape():
    data = requests.get(url).text
    soup = bs(data, 'html.parser')
    for item in soup.find_all('img'):
        if (len(stakes) == 0):
            _save_img(item['src'])
            continue
        for name in stakes:
            if name.capitalize() in item['src']:
                _save_img(item['src'])
                break
        
def read_stakes():
    file = open('.\stakes.txt')
    for line in file:
        if not is_blank(line):
            stakes.append(line.rstrip().lower())
    file.close()

def is_blank(line: str) -> bool:
    line = line.replace(" ", "")
    line = line.rstrip()
    return len(line) == 0

def _save_img(url: str):
    if (len(url) < 70):
        return
    data = requests.get(url).content
    img = open(f'img/{url[66:]}', 'wb')
    img.write(data)
    img.close

if __name__ == "__main__":
    read_stakes()
    scrape()