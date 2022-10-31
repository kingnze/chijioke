from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='entertainment'),
    path('entertainment/<slug:slug_id>/',views.entertainmentdetail,name='entertainmentdetail')
]