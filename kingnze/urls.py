from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('search',views.search,name='search'),
    path('headline',views.headline,name='headline'),
    path('bigstory',views.bigstory,name='bigstory'),
    path('trending',views.trending,name='trending'),
    path('politics',views.politics,name='politics'),
    path('crime',views.crime,name='crime'),
    path('business',views.business,name='business'),
    path('environment',views.environment,name='environment'),
    path('health',views.health,name='health'),
    path('contact',views.contact,name='contact'),
    path('tech',views.tech,name='tech'),
    path('headline/<slug:slug_id>/',views.headlinenewsdetail,name='headlinenewsdetail'),
    path('bigstory/<slug:slug_id>/',views.bigstorynewsdetail,name='bigstorynewsdetail'),
    path('trending/<slug:slug_id>/',views.trendingnewsdetail,name='trendingnewsdetail'),
    path('crime/<slug:slug_id>/',views.crimenewsdetail,name='crimenewsdetail'),
    path('environment/<slug:slug_id>/',views.environmentnewsdetail,name='environmentnewsdetail'),
    path('health/<slug:slug_id>/',views.healthnewsdetail,name='healthnewsdetail'),
    path('tech/<slug:slug_id>/',views.technewsdetail,name='technewsdetail'),
    path('business/<slug:slug_id>/',views.businessnewsdetail,name='businessnewsdetail'),
    path('politics/<slug:slug_id>/',views.politicsnewsdetail,name='politicsnewsdetail'),
]

