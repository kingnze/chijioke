from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='africanews'),
    path('africanews/<slug:slug_id>/',views.africanewsdetail,name='africanewsdetail')

]
