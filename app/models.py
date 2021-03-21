from django.db import models 
from django.db.models import Model 
from jsonfield import JSONField

  
class event(Model):
    title=models.CharField(max_length=200)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    description=models.CharField(max_length=500) 
    group=JSONField(default=None,null=True)
    url_nm = models.URLField()

class non_interestingurl(Model):
    url_name=models.URLField()
    bool=models.BooleanField(default=False)

class interestingurl(Model):
    title=models.CharField(max_length=200,null=True)
    start_time=models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True)
    description=models.CharField(max_length=500,null=True) 
    url_nm = models.URLField()
    group=JSONField(default=None,null=True)
    bool=models.BooleanField(default=False)

def __str__(self):
    return self.name