import os
from os import listdir
from os.path import isfile, join
import datetime
from pypinyin import lazy_pinyin
import json
from shutil import copyfile

# Get Date
now = datetime.datetime.now()

path_sufix = '_format'
emoji_path = r'.\\emoji'
hotword_path = r'.\\hotword'
tv_path = r'.\\tv'
girl_path = r'.\\2233'
# Here are three solutions for "SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape":
# r'C:\Users\expoperialed\Desktop\Python'
# 'C:\\Users\\expoperialed\\Desktop\\Python'
# 'C:/Users/expoperialed/Desktop/Python'

with open('index.json') as json_file:
    dict = json.load(json_file)

# Emoji
emoji_files = [f for f in listdir(emoji_path) if isfile(join(emoji_path, f))]

for f in emoji_files:
  if f != 'rename_all_files.py':
    file = f.replace('.png', '')
    if file not in dict:
      py = lazy_pinyin(file)
      name = ''
      for char in py:
        name = name + char
      dict[file] = 'bili_emoji_' + name
      copyfile(emoji_path + '/' + f, emoji_path + path_sufix + '/' + name + '.png')

# hotword
hotword_files = [f for f in listdir(hotword_path) if isfile(join(hotword_path, f))]

for f in hotword_files:
  if f != 'rename_all_files.py':
    file = f.replace('.png', '')
    if file not in dict:
      py = lazy_pinyin(file)
      name = ''
      for char in py:
        name = name + char
      dict[file] = 'bili_' + name
      copyfile(hotword_path + '/' + f, hotword_path + path_sufix + '/' + name + '.png')

# tv
tv_files = [f for f in listdir(tv_path) if isfile(join(tv_path, f))]

for f in tv_files:
  if f != 'rename_all_files.py':
    file = f.replace('.png', '')
    if file not in dict:
      py = lazy_pinyin(file)
      name = ''
      for char in py:
        name = name + char
      dict[file] = 'bili_' + name
      copyfile(tv_path + '/' + f, tv_path + path_sufix + '/' + name + '.png')

# 2233
girl_files = [f for f in listdir(girl_path) if isfile(join(girl_path, f))]

for f in girl_files:
  if f != 'rename_all_files.py':
    file = f.replace('.png', '')
    if file not in dict:
      py = lazy_pinyin(file)
      name = ''
      for char in py:
        name = name + char
      dict[file] = 'bili_' + name.replace('2233niang', '2233')
      copyfile(girl_path + '/' + f, girl_path + path_sufix + '/' + name + '.png')

# print(dict)

json = json.dumps(dict)
f = open("index.json","w")
f.write(json)
f.close()
