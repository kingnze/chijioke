from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='localnews'),
    path('localnews/<slug:slug_id>/',views.localnewsdetail,name='localnewsdetail')
]