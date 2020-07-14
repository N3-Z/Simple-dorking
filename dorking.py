import re
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import getopt,sys

bing_url = 'https://www.bing.com/search'
google_url = 'https://www.google.com/search'

page_ = 0
search_ = ''
engine_ =''

ua = UserAgent().random
headers = {
    'User-agent' : ua
}


def google():
    print("[+] google")
    payload = {
        'q' : search_,
        'start' : page_
    }
    req = requests.get(google_url, payload[0],headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    search_result = soup.find_all("div", class_='r')
    for link in search_result:
        print(link.find('a').attrs['href'])

def bing():
    print("[+] bing")
    payload = {
        'q' : search_,
        'first' : page_
    }
    req = requests.get(bing_url, payload, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    li = soup.find_all('li', class_="b_algo")

    for tag in li:
        print(tag.find('a').attrs['href'])

def main():
    global search_, page_, engine_
    args,_ = getopt.getopt(sys.argv[1:], "s:e:p:")
    for key,value in args:
        if key == "-s":
            search_ = value
        elif key == "-e":
            engine_ = value
        elif key == "-p":
            page_ = value
  
    if engine_ == "bing":
        bing()
    elif engine_ == "google":
        google()

if __name__ == '__main__':
    main()
    