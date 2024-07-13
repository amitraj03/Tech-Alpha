from django.shortcuts import render, redirect
from .models import URL
import string
import random

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        url = URL(original_url=original_url, short_url=short_url)
        url.save()
        return render(request, 'shortener/result.html', {'short_url': short_url})
    return render(request, 'shortener/index.html')

def redirect_to_url(request, short_url):
    url = URL.objects.get(short_url=short_url)
    return redirect(url.original_url)
