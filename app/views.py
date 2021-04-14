from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from . import models
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User




################################# index ######################################

@login_required()
def index(request):

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))




################################# pages ######################################

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




################################## maps ######################################

@login_required()
def maps(request):
    maps= models.Station.objects.all()
    mapbox_access_token = 'pk.eyJ1IjoiZG9yb3N0a2FyIiwiYSI6ImNrbmVjdzg3djFkb3EycG8wZW5sdjNld3YifQ.AeDSXrxKTXAxPdIEESuPqA'
    return render(request, 'ui-maps.html', {'maps': maps,'mapbox_access_token': mapbox_access_token})



################################ products ####################################

@login_required()
def products(request):
    products= models.Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required()
def products_detail(request, id):
    product = get_object_or_404(models.Product, id=id)
    nodes = models.Tree.objects.filter(relatedProduct=product)
    return render(request, 'products_detail.html', {'product': product,'nodes': nodes})




################################ stations ####################################

@login_required()
def stations(request):
    stations= models.Station.objects.all()
    return render(request, 'stations.html', {'stations': stations})


@login_required()
def stations_detail(request, id):
    product = get_object_or_404(models.Product, id=id)
    nodes = models.Tree.objects.filter(relatedProduct=product)
    return render(request, 'products_detail.html', {'product': product,'nodes': nodes})








    #nodes= models.Product.objects.filter(name__name='سوکت هالوژن')
    #nodes= models.Product.objects.filter(quantity=2)


##############################################################################
