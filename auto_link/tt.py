from bs4 import BeautifulSoup
import requests
import time

def change_link(link):
        if 'https://' in link:
            return link
        else:
            link = 'https://' + link
            return link

def valid_link(link):

    try:
        href = requests.get(link)
    except:
        return False
    else:
        return True


def countdown(t):
	while t:
		time.sleep(1)
		t -= 1
	return True


def get_ep_name(link):
    ref1 = link.index('/Episode')
    ref1 += 1
    ref2 = link.index('?')
    ep_name = link[ref1:ref2]
    epname = ep_name.replace('-', ' ')
    return epname






#t = input("Enter the time in seconds: ")
#countdown(int(t))
# html_text = 'https://kissasian.li/Drama/Squid-Game'
# href = requests.get(html_text).text
# soup = BeautifulSoup(href, 'lxml')
# links = soup.find_all('li', class_= 'episodeSub')
# print(links)