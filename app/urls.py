from django.urls import path 
from .views import home_view, event_view,crawl_view,scrape_view
  
urlpatterns = [ 
    path('', home_view ,name="urlsearch"),
    path('event',event_view,name="urlresult"),
    path('crawl',crawl_view,name="crawl"),
    path('scrape',scrape_view,name="scrape") 
] 