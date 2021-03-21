from django.shortcuts import render,redirect
from .event import basic,geturl,geturldata
from .models import event,non_interestingurl,interestingurl
import json


def home_view(request):
    return render(request, "home.html")

def event_view(request):
    # getdata()
    data= basic()
    for item in data:
        e=event(title= item['title'],start_time=item['start_time'],end_time=item['end_time'],description=item['description'],url_nm=item['url'],group=json.dumps(item['topic']))
        e.save()
    # get10urlsdata()
    
    return redirect("/")


def crawl_view(request):
    urlq=non_interestingurl.objects.filter(bool=False).values('url_name')[:1]
    url=urlq[0]['url_name']
    
    
    non_interestingurl.objects.filter(url_name=url).update(bool=True)
    data=geturl(url)
    d=data['interestingurl']
    for i in d:
        p=interestingurl(url_nm=i,bool=False)
        p.save()
    d2=data['non_interestingurl']
    for j in d2:
        q=non_interestingurl(url_name=j,bool=False)
        q.save()

    
    return redirect("/")

def scrape_view(request):
    uq=interestingurl.objects.filter(bool=False).values('url_nm')[:1]
    u=uq[0]['url_nm']
    dd=geturldata(u)
    interestingurl.objects.filter(url_nm=u).update(title= dd['title'],start_time=dd['start_time'],end_time=dd['end_time'],description=dd['description'],bool=True,group=json.dumps(dd['topic']))
    
    return redirect("/")
