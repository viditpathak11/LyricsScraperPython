import requests
import bs4
import sys


artist=input("artist: ").replace(" "," ")
song=input("song: ").replace(" "," ")


url='http://www.azlyrics.com/lyrics/%s/%s.html' % (artist,song)

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

res=requests.get(url,headers=headers)

try:
  res.raise_for_status()
except Exception as exc:
  print(exc)
  sys.exit()

print('\nconnected to %s' % url)

site=bs4.BeautifulSoup(res.text,"html.parser")

for lyrics in site.find_all("div", {"class":""}):
  print(lyrics.text)
