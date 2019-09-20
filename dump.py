from bs4 import BeautifulSoup
import urllib.request
import requests


#with open('http://10.5.5.9:8080/videos/DCIM/100GOPRO/') as fp:
#    soup = BeautifulSoup(fp, 'html.parser')

URL_BASE = 'http://10.5.5.9:8080'

url = URL_BASE + '/videos/DCIM/100GOPRO/'
r = requests.get(url)

soup = BeautifulSoup(r.text)

for link in soup.find_all('a'):
    href = link.get('href')
    if (href.endswith('.MP4') or href.endswith('.JPG')):
        filename = href.split('/')[-1] 

        urllib.request.urlretrieve(URL_BASE+href, 'data/'+filename)

print('done!')
