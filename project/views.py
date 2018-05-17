from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from interventi.models import Intervento, photo

# Create your views here.

def home(request):
    interventi = Intervento.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home.html', {'interventi': interventi})

def intervento_detail(request, slug, id):
    intervento = get_object_or_404(Intervento, slug=slug, id=id)
    intervento_data = Intervento.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    photo_upload = photo.objects.filter(author=intervento, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'intervento.html', {'intervento': intervento, 'photo_upload': photo_upload, 'intervento_data':intervento_data})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        projects_titolo = Intervento.objects.filter(sinonimi__icontains=q)
        #projects_sinonimi = Intervento.objects.filter(sinonimi__icontains=q)
        return render(request, 'search_results.html',{'projects_titolo': projects_titolo, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
