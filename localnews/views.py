from django.shortcuts import render
from .models import localnews
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
    local = localnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(local, 12)
    page = request.GET.get('page')
    paged_local = paginator.get_page(page)
    
    context = {
        'local': paged_local
    }

    return render(request,'localnews/localnews.html',context)  


def localnewsdetail(request,slug_id):
    thelocal =localnews.objects.filter(slug=slug_id).first()
    world = worldnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    africa = africanews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    local = localnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    sports = stportnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]

    context= {
      'post':thelocal,
      'world': world,
       'africa': africa,
       'local': local,
       'sports': sports,
       'enternews': enternews
  }
    return render(request,'localnews/local.html',context)
          