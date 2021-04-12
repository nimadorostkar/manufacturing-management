from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from . import models





@login_required()
def index(request):

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))



@login_required()
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))




@login_required()
def show(request):
    nodes= models.Tree.objects.all()
    #nodes= models.Product.objects.filter(name__name='سوکت هالوژن')
    #nodes= models.Product.objects.filter(quantity=2)
    return render(request, 'show1.html', {'nodes': nodes})





@login_required()
def maps(request):
    maps= models.Station.objects.all()
    return render(request, 'ui-maps.html', {'maps': maps})














#########################################################################
