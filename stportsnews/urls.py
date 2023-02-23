from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='sportsnews'),
    # path('search',views.search,name='search'),
    path('sportsnews/<slug:slug_id>/',views.sportsnewsdetail,name='sportsnewsdetail')
]


 
 