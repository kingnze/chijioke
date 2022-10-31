from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('ecommerce',views.ecommerce,name='ecommerce'),
    path('corporate',views.corporate,name='corporate'),
    path('magazine_blog',views.magazine_blog,name='magazine_blog'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('Web_development',views.Web_development,name='Web_development'),
    path('about',views.about,name='about'),
]

