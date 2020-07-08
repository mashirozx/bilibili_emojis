import os, requests, urllib.request

emoji_path = r'.\\emoji/'
hotword_path = r'.\\hotword/'
tv_path = r'.\\tv/'
girl_path = r'.\\2233/'

api = 'http://api.bilibili.com/x/emote/user/panel/web?business=dynamic'
api6 = 'http://api.bilibili.com/x/emote/package?business=reply&ids=6'

data = requests.get(api).json()

# print(data['data']['packages'][0])

for item in data['data']['packages'][0]['emote']:
  name = item['text'].replace('[','').replace(']','')
  url = item['url']
  file = emoji_path + name + '.png'
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)
    print('[' + name + ']')

for item in data['data']['packages'][1]['emote']:
  name = item['text'].replace('[','').replace(']','')
  url = item['url']
  file = hotword_path + name + '.png'
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)
    print('[' + name + ']')

for item in data['data']['packages'][2]['emote']:
  name = item['text'].replace('[','').replace(']','')
  url = item['url']
  file = tv_path + name + '.png'
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)
    print('[' + name + ']')

data = requests.get(api6).json()
for item in data['data']['packages'][0]['emote']:
  name = item['text'].replace('[','').replace(']','')
  url = item['url']
  file = girl_path + name + '.png'
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)
    print('[' + name + ']')