from django.contrib import admin
from .models import application, staff

class applicationadmin(admin.ModelAdmin):
    list_display = ['sn','applicant','location','recommending_officer' ]
    search_fields = ['applicant']


class staffadmin(admin.ModelAdmin):
    list_display = ['name','position','sex' ]
    search_fields = ['name']


admin.site.register(application, applicationadmin)
admin.site.register(staff, staffadmin)