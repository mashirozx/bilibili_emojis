import os,urllib.request
from bs4 import BeautifulSoup

emoji_path = r'.\\emoji/'
hotword_path = r'.\\hotword/'
tv_path = r'.\\tv/'
girl_path = r'.\\girl/'

f = open('tv.html', 'r', encoding="utf-8")
tv_html = f.read()
f.close()

f = open('2233.html', 'r', encoding="utf-8")
girl_html = f.read()
f.close()

f = open('emoji.html', 'r', encoding="utf-8")
emoji_html = f.read()
f.close()

f = open('hotword.html', 'r', encoding="utf-8")
hotword_html = f.read()
f.close()

tv_soup = BeautifulSoup(tv_html, features='html.parser')
for img in tv_soup.find_all('img'):
  name = img.get('title').replace('[','').replace(']','')
  url = img.get('src').replace('//','https://').replace('@112w_112h.webp','')
  file = tv_path + name + '.png'
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)
    print('[' + name + ']')

hotword_soup = BeautifulSoup(hotword_html, features='html.parser')
for img in hotword_soup.find_all('img'):
  name = img.get('title').replace('[','').replace(']','')
  url = img.get('src').replace('//','https://').replace('@112w_112h.webp','')
  file = hotword_path + name + '.png'
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)
    print('[' + name + ']')

girl_soup = BeautifulSoup(girl_html, features='html.parser')
for img in girl_soup.find_all('img'):
  name = img.get('title').replace('[','').replace(']','')
  url = img.get('src').replace('//','https://').replace('@112w_112h.webp','')
  file = girl_path + name + '.png'
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)
    print('[' + name + ']')

emoji_soup = BeautifulSoup(emoji_html, features='html.parser')
for img in emoji_soup.find_all('img'):
  name = img.get('title').replace('[','').replace(']','')
  url = img.get('src').replace('//','https://').replace('@112w_112h.webp','')
  file = emoji_path + name + '.png'
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)
    print('[' + name + ']')