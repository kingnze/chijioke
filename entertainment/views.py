from django.shortcuts import render,redirect
from entertainment.forms import entertainmentForm
from .models import entertainment,entertainmentComment
from worldnews.models import worldnews
from worldnews.views import worldnews
from kingnze.models import Headline, Business, Bigstory, Trending, Crime, Environment, Health, Tech,Comment,Reply
from kingnze.views import Headline, Business, Bigstory, Trending, Crime, Environment, Health, Tech
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
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(enternews, 12)
    page = request.GET.get('page')
    paged_enternews = paginator.get_page(page)
    
    context = {
        'enternews': paged_enternews,
    }

    return render(request,'entertainment/entertainment.html',context)  


def entertainmentdetail(request,slug_id):
    theentertainment =entertainment.objects.filter(slug=slug_id).first()
    world = worldnews.objects.order_by('-date_posted').filter(published=True)[:1]
    africa = africanews.objects.order_by('-date_posted').filter(published=True)[:1]
    local = localnews.objects.order_by('-date_posted').filter(published=True)[:1]
    sports = stportnews.objects.order_by('-date_posted').filter(published=True)[:1]
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True)[:1]
    headline = Headline.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    business = Business.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    bigstory = Bigstory.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    trending = Trending.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    crime = Crime.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    environment = Environment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    health = Health.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    tech = Tech.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    enterComment = entertainmentComment.objects.order_by('-date_posted').filter(post__id = theentertainment.id)
    form = entertainmentForm()
    if request.method == 'POST':
        form = entertainmentForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.entertainmentusercomment = request.user
            thecomment.post = theentertainment
            thecomment.save()

            return redirect('entertainmentdetail',theentertainment.slug)
    context= {
        'post':theentertainment,
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
        'entertainmentComments':enterComment
  }
    return render(request,'entertainment/enternews.html',context)      