from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

def error_404(request, exception):
    return render(request, 'error_404.html')

def error_500(request):
    return render(request, 'error_500.html')

def pine_portfolio(request):
    return render(
        request,
        'pinytree/pine_portfolio.html'
    )