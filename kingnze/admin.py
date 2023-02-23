from django.contrib import admin
from .models import  Business, Contact,Headline,Bigstory ,Crime ,Environment ,Health, Trending,Tech,Comment,Commet, Reply,BusinessComment,Politics,PoliticsComment,CrimeCommemt,EnvironmentComment,HealthComment,TrendingComment,TechComment


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone', 'email')
    list_display_links = ('id', 'fullname',)
    search_fields = ('fullname', 'phone', 'email')
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)
admin.site.register(Headline)
admin.site.register(Trending)
admin.site.register(Bigstory)
admin.site.register(Crime)
admin.site.register(Environment)
admin.site.register(Health)
admin.site.register(Business)
admin.site.register(Tech)
admin.site.register(Comment)
admin.site.register(Commet)
admin.site.register(BusinessComment)
admin.site.register(Politics)
admin.site.register(PoliticsComment)
admin.site.register(CrimeCommemt)
admin.site.register(EnvironmentComment)
admin.site.register(HealthComment)
admin.site.register(TrendingComment)
admin.site.register(TechComment)
admin.site.register(Reply)