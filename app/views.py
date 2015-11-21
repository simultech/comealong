from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

from django.http import HttpResponse

def index(request):
    template = loader.get_template('app/index.html')
    data = {
        'friend': 'princess strawberry'
    }
    context = RequestContext(request, data)
    return HttpResponse(template.render(context))