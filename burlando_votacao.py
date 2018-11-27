import requests
import random

def proxies():
    url = 'http://gimmeproxy.com/api/getProxy'
    r = requests.get(url).json()
    proxy = r['curl']
    protocol = r['protocol']
    print proxy

    return {protocol:proxy}

#proxies = proxies()
#r = requests.get('http://ipinfo.io', proxies=proxies)
#print r.content
