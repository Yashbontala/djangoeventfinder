import requests
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url
from .group import find_topic
import re


"""for eventbrite.com"""


def get_metadata(url):
    """Fetch JSON-LD structured data."""
    reqs = requests.get(url)
    html = reqs.text
    metadata = extruct.extract(
        html,
        base_url=get_base_url(url),
        syntaxes=['json-ld'],
        uniform=True
    )['json-ld']
    if bool(metadata) and isinstance(metadata, list):
        metadata = metadata[0]

    return metadata

def basic():
    x=get10urlsdata('https://www.eventbrite.com/d/online/events/')
    y=get10urlsdata('https://www.naadyogacouncil.com/en/events/')
    z=get10urlsdata('https://insider.in/online')

    return x+y+z

def get10urlsdata(u):
    
    
    dard=geturl(u)
    urls_final = dard['interestingurl']
    print("for eventbrite.com ")
    print("data for meta data\n")
    data=[]
    for i in range(0, 10):
        metadata=get_metadata(urls_final[i])
        d={}
        d['title']=metadata['name']
        d['description']=metadata['description']
        d['start_time']=metadata['startDate']
        d['end_time']=metadata['endDate']
        d['url']=urls_final[i]
        d['topic']=find_topic(d['description'])
        data.append(d)
        # print(metadata)
        # print(find_topic(description))2
    return data

def geturldata(u):
    metadata=get_metadata(u)
    d={}
    d['title']=metadata['name']
    d['description']=metadata['description']
    d['start_time']=metadata['startDate']
    d['end_time']=metadata['endDate']
    d['url']=u
    d['topic']=find_topic(d['description'])
    return d


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
def geturl(u):
    
    reqs=requests.get(u,headers=headers)
    soup=BeautifulSoup(reqs.content, 'html.parser')
    base_Url='https://'
    urlsf=[item.get('href') for item in soup.find_all('a')]
    urls=list(dict.fromkeys(urlsf))
    urls = list(filter(None, urlsf)) 
    pat='(https://www\\.eventbrite\\.(com|co.uk)/e/(.+?)|https://insider\\.in/(.+?)/event$|https://www\\.naadyogacouncil\\.com/en/event-single/(.+?))'
    interesting_url=[]
    non_interestingurl=[]
    for url in urls:
        if not re.match(base_Url,url):
            url='https://insider.in' + url
        if re.match(pat,url):
            interesting_url.append(url)
        else:
            non_interestingurl.append(url)
    typesofurl={}
    typesofurl['interestingurl']=interesting_url
    typesofurl['non_interestingurl']=non_interestingurl
    return typesofurl

        
        

