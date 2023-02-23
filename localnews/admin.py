from django.contrib import admin
from .models import localnews,localnewsComment

# Register your models here.


class localnewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_posted', 'author')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'date_posted', 'author')
    list_per_page = 10

admin.site.register(localnews, localnewsAdmin)
admin.site.register(localnewsComment)
