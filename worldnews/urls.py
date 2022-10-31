from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='worldnews'),
    path('worldnews/<slug:slug_id>/',views.worldnewsdetail,name='worldnewsdetail')

    
]















