from django.shortcuts import render
from .models import stportnews
from worldnews.models import worldnews
from worldnews.views import worldnews
from africanews.models import africanews
from africanews.views import africanews
from localnews.models import localnews
from localnews.views import localnews
from stportsnews.models import stportnews
from stportsnews.views import stportnews
from entertainment.models import entertainment
from entertainment.views import entertainment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.



def index(request):
    sports = stportnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(sports, 12)
    page = request.GET.get('page')
    paged_sports = paginator.get_page(page)
    
    context = {
        'sports': paged_sports
    }

    return render(request,'sportsnews/sportsnews.html',context) 


def sportsnewsdetail(request,slug_id):
    thesport =stportnews.objects.filter(slug=slug_id).first()
    world = worldnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    africa = africanews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    local = localnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    sports = stportnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]

    context= {
      'post':thesport,
      'world': world,
       'africa': africa,
       'local': local,
       'sports': sports,
       'enternews': enternews
  }
    return render(request,'sportsnews/sport.html',context)    