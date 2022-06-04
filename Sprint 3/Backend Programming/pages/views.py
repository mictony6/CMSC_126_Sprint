from multiprocessing import context
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from pages.forms import RequestForm

from pages.models import ArtWork

# Create your views here.


def home_view(request, *args, **kwargs):
    context = {
        'featured': ArtWork.objects.filter(featured=True)
    }
    return render(request, 'home.html', context)


def about_view(request):
    context = {}
    return render(request, 'about.html', context)


def commissions_view(request, *args, **kwargs):
    context = {
        'artworks': ArtWork.objects.all()
    }
    return render(request, 'commissions.html', context)


def detail_view(request, pk):
    context = {
        'subject': get_object_or_404(ArtWork, pk=pk)
    }
    return render(request, 'detail.html', context)


def request_form_view(request, *args, **kwargs):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('redirect')
    context = {
        'form': form
    }
    return render(request, 'request_form.html', context)


def redirect_page(request):
    return render(request, 'redirect_page.html', {})
