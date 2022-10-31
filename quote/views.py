from django.shortcuts import render
from . models import Freequote
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.


def index(request):
    Freequotes = Freequote.objects.order_by('-date_posted').filter(is_published=True)

    paginator = Paginator(Freequotes, 15)
    page = request.GET.get('page')
    paged_Freequotes = paginator.get_page(page)

    context = {'Freequotes': paged_Freequotes}

    return render(request,'quote/Freequote.html',context)  

