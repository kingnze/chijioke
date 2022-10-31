from django.contrib import admin
from .models import stportnews

# Register your models here.


class stportnewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_posted', 'author')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'date_posted', 'author')
    list_per_page = 10


admin.site.register(stportnews, stportnewsAdmin)
