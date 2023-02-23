from django.shortcuts import render,redirect
from stportsnews.forms import stportnewsForm
from .models import stportnews,stportnewsComment
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
    sports = stportnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(sports, 12)
    page = request.GET.get('page')
    paged_sports = paginator.get_page(page)
    
    context = {
        'sports': paged_sports,
    }

    return render(request,'sportsnews/sportsnews.html',context) 


def sportsnewsdetail(request,slug_id):
    thesports =stportnews.objects.filter(slug=slug_id).first()
    world = worldnews.objects.order_by('-date_posted').filter(published=True)[:1]
    africa = africanews.objects.order_by('-date_posted').filter(published=True)[:1]
    local = localnews.objects.order_by('-date_posted').filter(published=True)[:1]
    sports = stportnews.objects.order_by('-date_posted').filter(published=True)[:1]
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True)[:1]
    headline = Headline.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    business = Business.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    bigstory = Bigstory.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    trending = Trending.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    crime = Crime.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    environment = Environment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    health = Health.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    tech = Tech.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    stportComment = stportnewsComment.objects.order_by('-date_posted').filter(post__id = thesports.id)
    form = stportnewsForm()
    if request.method == 'POST':
        form = stportnewsForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.stportnewsusercomment = request.user
            thecomment.post = thesports
            thecomment.save()

            return redirect('sportsnewsdetail',thesports.slug)

    context= {
      'post':thesports,
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
        'stportnewsComments':stportComment
  }
    return render(request,'sportsnews/sport.html',context)       