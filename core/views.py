from django.shortcuts import render

def error_404(request, exception):
    return render(request, 'error_404.html')

def error_500(request):
    return render(request, 'error_500.html')