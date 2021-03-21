from django.contrib import admin
from .models import event, non_interestingurl ,interestingurl

admin.site.register(event)
admin.site.register(non_interestingurl)
admin.site.register(interestingurl)
# Register your models here.
