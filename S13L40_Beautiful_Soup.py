import bs4
import requests

def getWebPrice(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('.uc-price')
    return elems[0].text.strip()

price = getWebPrice('https://nostarch.com/automatestuff')
print('The price is {}'.format(price))

