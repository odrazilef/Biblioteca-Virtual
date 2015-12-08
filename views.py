
#sitiolectura/biblioteca/views.py
from django.http import HttpResponse
# Create your views here.

def primer_vista(request):#siempre recibe un parámetro HttpRequest
    return HttpResponse("Hola, soy tu primer proyecto en Django")
