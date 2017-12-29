from bs4 import BeautifulSoup
import lxml
import requests
import re

username = 'thejackalbot'
client_id = ''
token = ''
channel = 'fremily'

url = 'https://api.twitch.tv/helix/users?login=' + channel
headers = {'Client-ID': client_id, 'Authorization': 'OAuth ' + token}
r = requests.get(url, headers=headers).json()
user_id = r['data'][0]['id']
url2 = 'https://api.twitch.tv/helix/streams?user_id=' + user_id
s = requests.get(url2, headers=headers).json()
game_id = s['data'][0]['game_id']
url3 = 'https://api.twitch.tv/helix/games?id=' + game_id
g = requests.get(url3, headers=headers).json()
gamename = g['data'][0]['name']
humble = requests.get('http://www.humblebundle.com/store/' +gamename.lower().replace(' ', '-')).text
soup = BeautifulSoup(humble,'lxml')
thislink = ''
for tag in soup.find_all('title'):
    match = re.match('Page not found', str(tag.contents))
    if match:
        continue
    else:
        thislink = gamename + ' is available on the Humble Store here: http://www.humblebundle.com/store/' + \
                   gamename.lower().replace(' ', '-') + '?partner=' + channel + '&charity=31440'
print(thislink)
