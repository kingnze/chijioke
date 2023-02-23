from django.shortcuts import render,redirect
from africanews.forms import africanewsForm
from .models import africanews,africanewsComment
from kingnze.models import Headline, Business, Bigstory, Trending, Crime, Environment, Health, Tech,Reply
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



# Create your views here.


def index(request):
    africa = africanews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(africa, 12)
    page = request.GET.get('page')
    paged_africa = paginator.get_page(page)
    
    context = {
        'africa': paged_africa,

    }

    return render(request,'africanews/africanews.html',context)  


def africanewsdetail(request,slug_id):
    theafricanews =africanews.objects.filter(slug=slug_id).first()
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
    africanComment = africanewsComment.objects.order_by('-date_posted').filter(post__id = theafricanews.id)
    form = africanewsForm()
    if request.method == 'POST':
        form = africanewsForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.africanewsusercomment = request.user
            thecomment.post = theafricanews
            thecomment.save()

            return redirect('africanewsdetail',theafricanews.slug)

    context= {
        'post':theafricanews,
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
        'africanewsComments':africanComment

  }
    return render(request,'africanews/africa.html',context)