from django.http import HttpResponse

def home( request ):
    return HttpResponse('<h2>Bienvenidos</h2>')