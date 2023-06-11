from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

def error_404(request, exception):
    return render(request, 'error_404.html')

def error_500(request):
    return render(request, 'error_500.html')

@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request: HttpRequest) -> HttpResponse:
    file = (settings.BASE_DIR / "static" / "images/bimbimka_feather-ai2.svg").open("rb")
    return FileResponse(file)