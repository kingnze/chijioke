from django.contrib import admin
from .models import  Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone', 'email')
    list_display_links = ('id', 'fullname',)
    search_fields = ('fullname', 'phone', 'email')
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)