from django.shortcuts import render
from .models import africanews
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
    africa = africanews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(africa, 12)
    page = request.GET.get('page')
    paged_africa = paginator.get_page(page)
    
    context = {
        'africa': paged_africa
    }

    return render(request,'africanews/africanews.html',context)  


def africanewsdetail(request,slug_id):
    thelocal =africanews.objects.filter(slug=slug_id).first()
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
    return render(request,'africanews/africa.html',context)

