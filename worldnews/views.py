from django.shortcuts import render,redirect
from worldnews.forms import worldnewsForm
from .models import worldnews,worldnewsComment
from kingnze.models import Headline, Business, Bigstory, Trending,Comment,Reply
from kingnze.views import Headline, Business, Bigstory, Trending
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
    world = worldnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(world, 16)
    page = request.GET.get('page')
    paged_world = paginator.get_page(page)
    
    context = {
        'world': paged_world
    }

    return render(request,'worldnews/worldnews.html',context)   



def worldnewsdetail(request,slug_id):
    theworld = worldnews.objects.filter(slug=slug_id).first()
    world = worldnews.objects.order_by('-date_posted').filter(published=True)[:1]
    africa = africanews.objects.order_by('-date_posted').filter(published=True)[:1]
    local = localnews.objects.order_by('-date_posted').filter(published=True)[:1]
    sports = stportnews.objects.order_by('-date_posted').filter(published=True)[:1]
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True)[:1]
    headline = Headline.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    business = Business.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    bigstory = Bigstory.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    trending = Trending.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    worldComment = worldnewsComment.objects.order_by('-date_posted').filter(post__id = theworld.id)
    form = worldnewsForm()
    if request.method == 'POST':
        form = worldnewsForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.worldnewsusercomment = request.user
            thecomment.post = theworld
            thecomment.save()

            return redirect('worldnewsdetail',theworld.slug)

    context= {
      'post':theworld,
      'world': world,
       'africa': africa,
       'local': local,
       'sports': sports,
       'enternews': enternews,
        'world': world,
        'africa': africa,
        'local': local,
        'sports': sports,
        'enternews': enternews,
        'headline':headline,
        'bigstory':bigstory,
        'trending':trending,
        'business':business,
        'form':form,
        'worldnewsComments':worldComment
  }
    return render(request,'worldnews/world.html',context)

def quote(request,slug_id):

    context= {}
    return render(request,'worldnews/quote.html',context)