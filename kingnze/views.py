from django.shortcuts import render, redirect 
from .models import Contact,Headline,Bigstory,Trending,Crime,Environment,Health,Business ,Tech,Comment,Commet,Politics,BusinessComment,CrimeCommemt,TrendingComment,EnvironmentComment,PoliticsComment,HealthComment,TechComment
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
from quote.models import Freequote
from quote.views import Freequote
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import CommentForm,CommetForm,CrimeForm,BusinessForm,TrendingForm,EnvironmentForm,PoliticsForm,HealthForm,TechForm
from django.contrib.auth.decorators import login_required


def search(request):
    query = request.GET.get('q')
    if query:
        results1 = Headline.objects.filter(title=query)
        results2 = Bigstory.objects.filter(title=query)
        results3 = Trending.objects.filter(title=query)
        results4 = Crime.objects.filter(title__icontains=query)
        results5 = Environment.objects.filter(title__icontains=query)
        results6 = Health.objects.filter(title__icontains=query)
        results7 = Tech.objects.filter(title__icontains=query)
        results8 = Politics.objects.filter(title__icontains=query)
        results9 = worldnews.objects.filter(title__icontains=query)
        results10 = africanews.objects.filter(title__icontains=query)
        results11 = localnews.objects.filter(title__icontains=query)
        results12 = stportnews.objects.filter(title__icontains=query)
        results13 = entertainment.objects.filter(title__icontains=query)
    else:
        results1 = Headline.objects.none()
        results2 = Bigstory.objects.none()
        results3 = Trending.objects.none()
        results4 = Crime.objects.none()
        results5 = Environment.objects.none()
        results6 = Health.objects.none()
        results7 = Tech.objects.none()
        results8 = Politics.objects.none()
        results9 = worldnews.objects.none()
        results10 = africanews.objects.none()
        results11 = localnews.objects.none()
        results12 = stportnews.objects.none()
        results13 = entertainment.objects.none()

    context = {
        'query': query, 
        'results1': results1, 
        'results2': results2, 
        'results3': results3,
        'results4': results4, 
        'results5': results5, 
        'results6': results6,
        'results7': results7,
        'results8': results8,
        'results9': results9,
        'results10': results10,
        'results11': results11,
        'results12': results12,
        'results13': results13,
        }
      
    return render(request,'kingnze/search.html',context)


# def search(request):
#     keywords = request.GET['mysearch']
#     searchesult = Headline.objects.filter(title__icontains = keywords)
#     searchesult = Business.objects.filter(title__icontains = keywords)
#     searchesult = Bigstory.objects.filter(title__icontains = keywords)
#     searchesult = Trending.objects.filter(title__icontains = keywords)
#     searchesult = Crime.objects.filter(title__icontains = keywords)
#     searchesult = Environment.objects.filter(title__icontains = keywords)
#     searchesult = Health.objects.filter(title__icontains = keywords)
#     searchesult = Tech.objects.filter(title__icontains = keywords)
#     searchesult = Politics.objects.filter(title__icontains = keywords)


#     context = {
#         'results':searchesult
#     }

#     return render(request,'kingnze/search.html',context)

def index(request):
    world = worldnews.objects.order_by('-date_posted').filter(published=True)[:1]
    africa = africanews.objects.order_by('-date_posted').filter(published=True)[:1]
    local = localnews.objects.order_by('-date_posted').filter(published=True)[:1]
    sports = stportnews.objects.order_by('-date_posted').filter(published=True)[:1]
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True)[:1]
    headline = Headline.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    business = Business.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    bigstory = Bigstory.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    trending = Trending.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:4]
    Freequotes = Freequote.objects.order_by('date_posted').filter(is_published=True)[:1]
    crime = Crime.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    environment = Environment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    health = Health.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    tech = Tech.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:2]
    politics = Politics.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]

    
    context = {
        'world': world,
        'africa': africa,
        'local': local,
        'sports': sports,
        'enternews': enternews,
        'headline':headline,
        'Freequotes': Freequotes,
        'bigstory':bigstory,
        'trending':trending,
        'crime':crime,
        'environment':environment,
        'health':health,
        'business':business,
        'tech':tech,
        'politics':politics
    
    }

    return render(request,'kingnze/index.html',context)

def headline(request):
    headline = Headline.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(headline, 12)
    page = request.GET.get('page')
    paged_headline = paginator.get_page(page)

    context= {
        'headline':paged_headline,
    }
    return render(request,'kingnze/headline.html',context)  

def headlinenewsdetail(request,slug_id):
    theheadline =Headline.objects.filter(slug=slug_id).first()
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
    postcomments = Comment.objects.order_by('-date_posted').filter(post__id = theheadline.id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.usercomment = request.user
            thecomment.post = theheadline
            thecomment.save()

            return redirect('headlinenewsdetail',theheadline.slug)

    context= {
        'post':theheadline,
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
        'comments':postcomments

  }
    return render(request,'kingnze/headlinenews.html',context)

def business(request):
    business = Business.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(business, 12)
    page = request.GET.get('page')
    paged_business = paginator.get_page(page)

    context= {
        'business':paged_business,
    }
    return render(request,'kingnze/business.html',context)  

def businessnewsdetail(request,slug_id):
    thebusiness = Business.objects.filter(slug=slug_id).first()
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
    businessComment = BusinessComment.objects.order_by('-date_posted').filter(post__id = thebusiness.id)
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.Businessusercomment = request.user
            thecomment.post = thebusiness
            thecomment.save()

            return redirect('businessnewsdetail',thebusiness.slug)
    

    context= {
        'post':thebusiness,
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
        'BusinessComments':businessComment

  }
    return render(request,'kingnze/businessnews.html',context)

def bigstory(request):
    bigstory = Bigstory.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
   

    paginator = Paginator(bigstory, 12)
    page = request.GET.get('page')
    paged_bigstory = paginator.get_page(page)

    context= {
 
        'bigstory':paged_bigstory,
    }
    return render(request,'kingnze/bigstory.html',context)  

def bigstorynewsdetail(request,slug_id):
    thebigstory = Bigstory.objects.filter(slug=slug_id).first()
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
    postcommet = Commet.objects.order_by('-date_posted').filter(post__id = thebigstory.id)
    form = CommetForm()
    if request.method == 'POST':
        form = CommetForm(request.POST)
        if form.is_valid():
            tcomment = form.save(commit=False)
            tcomment.usercommet = request.user
            tcomment.post = thebigstory
            tcomment.save()

            return redirect('bigstorynewsdetail',thebigstory.slug)

    context= {
        'post':thebigstory,
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
        'commet':postcommet

  }
    return render(request,'kingnze/bigstorynews.html',context)

def trending(request):
    trending = Trending.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]

    paginator = Paginator(trending, 12)
    page = request.GET.get('page')
    paged_trending = paginator.get_page(page)

    context= {
        'trending':paged_trending,

    }
    return render(request,'kingnze/trending.html',context)  

def trendingnewsdetail(request,slug_id):
    thetrending =Trending.objects.filter(slug=slug_id).first()
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
    postcommts = TrendingComment.objects.order_by('-date_posted').filter(post__id = thetrending.id)
    form = TrendingForm()
    if request.method == 'POST':
        form = TrendingForm(request.POST)
        if form.is_valid():
            tecomment = form.save(commit=False)
            tecomment.Trendingusercomment = request.user
            tecomment.post = thetrending
            tecomment.save()

            return redirect('trendingnewsdetail',thetrending.slug)

    context= {
        'post':thetrending,
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
        'TrendingComments':postcommts

  }
    return render(request,'kingnze/trendingstory.html',context)

def crime(request):
    crime = Crime.objects.order_by('-date_posted').filter(published=True).filter(flag=False)


    paginator = Paginator(crime, 12)
    page = request.GET.get('page')
    paged_crime = paginator.get_page(page)

    context= {
        'crime':paged_crime,

    }
    return render(request,'kingnze/crime.html',context) 

def crimenewsdetail(request,slug_id):
    thecrime =Crime.objects.filter(slug=slug_id).first()
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
    crimeCommemts = CrimeCommemt.objects.order_by('-date_posted').filter(post__id = thecrime.id)
    form = CrimeForm()
    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.Crimeusercomment = request.user
            thecomment.post = thecrime
            thecomment.save()

            return redirect('crimenewsdetail',thecrime.slug)

    context= {
        'post':thecrime,
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
        'CrimeComments':crimeCommemts

  }
    return render(request,'kingnze/crimenews.html',context)

def environment(request):
    environment = Environment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(environment, 12)
    page = request.GET.get('page')
    paged_environment = paginator.get_page(page)

    context= {

        'environment':paged_environment,
    }
    return render(request,'kingnze/environment.html',context)  

def environmentnewsdetail(request,slug_id):
    theenvironment =Environment.objects.filter(slug=slug_id).first()
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
    environmentComment = EnvironmentComment.objects.order_by('-date_posted').filter(post__id = theenvironment.id)
    form = EnvironmentForm()
    if request.method == 'POST':
        form = EnvironmentForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.Environmentusercomment = request.user
            thecomment.post = theenvironment
            thecomment.save()

            return redirect('environmentnewsdetail',theenvironment.slug)

    context= {
        'post':theenvironment,
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
        'EnvironmentComments':environmentComment

  }
    return render(request,'kingnze/environmentnews.html',context)

def politics(request):
    politics = Politics.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(politics, 12)
    page = request.GET.get('page')
    paged_politics = paginator.get_page(page)

    context= {

        'politics':paged_politics,
    }
    return render(request,'kingnze/politics.html',context)  

def politicsnewsdetail(request,slug_id):
    thepolitics =Politics.objects.filter(slug=slug_id).first()
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
    politicsComment = PoliticsComment.objects.order_by('-date_posted').filter(post__id = thepolitics.id)
    form = PoliticsForm()
    if request.method == 'POST':
        form = PoliticsForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.Politicsusercomment = request.user
            thecomment.post = thepolitics
            thecomment.save()

            return redirect('politicsnewsdetail',thepolitics.slug)

    context= {
        'post':thepolitics,
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
        'PoliticsComments':politicsComment

  }
    return render(request,'kingnze/politicsnews.html',context)

def health(request):
    health = Health.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(health, 12)
    page = request.GET.get('page')
    paged_health = paginator.get_page(page)

    context= {
        'health':paged_health,
    }
    return render(request,'kingnze/health.html',context)  

def healthnewsdetail(request,slug_id):
    thehealth =Health.objects.filter(slug=slug_id).first()
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
    healthComment = HealthComment.objects.order_by('-date_posted').filter(post__id = thehealth.id)
    form = HealthForm()
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.Healthusercomment = request.user
            thecomment.post = thehealth
            thecomment.save()

            return redirect('healthnewsdetail',thehealth.slug)

    context= {
        'post':thehealth,
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
        'HealthComments':healthComment

  }
    return render(request,'kingnze/healthnews.html',context)

def tech(request):
    tech = Tech.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(tech, 12)
    page = request.GET.get('page')
    paged_tech = paginator.get_page(page)

    context= {
        'tech':paged_tech,
    }
    return render(request,'kingnze/tech.html',context)   

def technewsdetail(request,slug_id):
    thetech =Tech.objects.filter(slug=slug_id).first()
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
    techComment = TechComment.objects.order_by('-date_posted').filter(post__id = thetech.id)
    form = TechForm()
    if request.method == 'POST':
        form = TechForm(request.POST)
        if form.is_valid():
            thecomment = form.save(commit=False)
            thecomment.Techusercomment = request.user
            thecomment.post = thetech
            thecomment.save()

            return redirect('technewsdetail',thetech.slug)

    context= {
        'post':thetech,
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
        'TechComments':techComment

  }
    return render(request,'kingnze/technews.html',context)

def contact(request):
  if request.method == 'POST':
    
      try:
          connect = Contact(fullname=request.POST['fullname'],phone=request.POST['phone'],email=request.POST['email'],message=request.POST['message'])
          messages.success(request,f"{request.POST['fullname']} Sent Successfully!!")

          connect.save()
          return redirect('contact')

      except Exception as e:
          messages.error(request,f"Something went wrong...")

  return render(request,'kingnze/contact.html')    

