from django.shortcuts import render, redirect
from .models import Contact
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

# Create your views here.
def index(request):
    world = worldnews.objects.order_by('-date_posted').filter(published=True)[:2]
    africa = africanews.objects.order_by('-date_posted').filter(published=True)[:2]
    local = localnews.objects.order_by('-date_posted').filter(published=True)[:2]
    sports = stportnews.objects.order_by('-date_posted').filter(published=True)[:2]
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True)[:2]
    Freequotes = Freequote.objects.order_by('date_posted').filter(is_published=True)[:1]
    
    context = {
        'world': world,
        'africa': africa,
        'local': local,
        'sports': sports,
        'enternews': enternews,
        'Freequotes': Freequotes,
    }

    return render(request,'kingnze/index.html',context)


def services(request):
 
 
  contex = {
    
  }
  return render(request,'kingnze/services.html',contex)  


def ecommerce(request):
 
 
  contex = {
    
  }
  return render(request,'kingnze/ecommerce.html',contex)  


def corporate(request):
 
 
  contex = {
    
  }
  return render(request,'kingnze/corporate.html',contex)  


def Web_development(request):
 
 
  contex = {
    
  }
  return render(request,'kingnze/Web_development.html',contex)  

def magazine_blog(request):
 
 
  contex = {
    
  }
  return render(request,'kingnze/magazine_blog.html',contex)  

def portfolio(request):
 
 
  contex = {
    
  }
  return render(request,'kingnze/portfolio.html',contex)  



def about(request):
 
 
  contex = {
    
  }
  return render(request,'kingnze/about.html',contex)    


def contact(request):
 
 
  contex = {
    
  }
  return render(request,'kingnze/contact.html',contex)    


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


