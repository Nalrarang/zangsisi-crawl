import requests
import datetime
from bs4 import BeautifulSoup

date = datetime.date.today()
today = date.strftime("%m/%d")
print today

r = requests.get('http://zangsisi.net/')

plain_text = r.text

soup = BeautifulSoup(plain_text, 'html.parser')
recent_list = soup.select('#recent-manga')

for selector in recent_list:
    for a in selector.select('.list'):
        for b in a.select('.date'):
            if today == b.string:
                print "★☆★☆" + today + " 만화 리스트★☆★☆"
                for c in a.select('.contents > a'):
                    print c.contents[0], c.contents[1].string
