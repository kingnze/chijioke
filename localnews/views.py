from django.shortcuts import render,redirect
from localnews.forms import localnewsForm
from .models import localnews,localnewsComment
from kingnze.models import Headline, Business, Bigstory, Trending, Crime, Environment, Health, Tech,Comment,Reply
from kingnze.views import Headline, Business, Bigstory, Trending, Crime, Environment, Health, Tech
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



def index(request):
    local = localnews.objects.order_by('-date_posted').filter(published=True)


    paginator = Paginator(local, 12)
    page = request.GET.get('page')
    paged_local = paginator.get_page(page)
    
    context = {
        'local': paged_local,
    }

    return render(request,'localnews/localnews.html',context)  


def localnewsdetail(request,slug_id):
    thelocal =localnews.objects.filter(slug=slug_id).first()
    world = worldnews.objects.order_by('-date_posted').filter(published=True)[:1]
    africa = africanews.objects.order_by('-date_posted').filter(published=True)[:1]
    local = localnews.objects.order_by('-date_posted').filter(published=True)[:1]
    sports = stportnews.objects.order_by('-date_posted').filter(published=True)[:1]
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True)[:1]
    headline = Headline.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    business = Business.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    bigstory = Bigstory.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    trending = Trending.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    crime = Crime.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    environment = Environment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    health = Health.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    tech = Tech.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    localComment = localnewsComment.objects.order_by('-date_posted').filter(post__id = thelocal.id)
    form = localnewsForm()
    if request.method == 'POST':
        form = localnewsForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.localnewsusercomment = request.user
            thecomment.post = thelocal
            thecomment.save()

            return redirect('localnewsdetail',thelocal.slug)
    context= {
      'post':thelocal,
      'world': world,
        'africa': africa,
        'local': local,
        'sports': sports,
        'enternews': enternews,
        'headline':headline,
        'bigstory':bigstory,
        'trending':trending,
        'crime':crime,
        'environment':environment,
        'health':health,
        'business':business,
        'tech':tech,
        'form':form,
        'localnewsComments':localComment
  }
    return render(request,'localnews/local.html',context)  
          