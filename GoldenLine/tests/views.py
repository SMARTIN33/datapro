from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.


def index(request):
    context=Context({"applicationname":"Application Goldenline","Utilisateurs":["Franck", "Isa", "Victor"]})
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render(context.flatten()))