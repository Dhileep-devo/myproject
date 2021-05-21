from django.contrib import admin
from .models import FeedFile,Feed
# Register your models here.
class FeedAdmin(admin.ModelAdmin):
    list_display=['user','text']
admin.site.register(Feed,FeedAdmin)
class FeedFileAdmin(admin.ModelAdmin):
    list_display=['file','feed']

admin.site.register(FeedFile,FeedFileAdmin)