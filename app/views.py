from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from . import models
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import ugettext_lazy as _
from .forms import ProfileForm, UserForm



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
    station = get_object_or_404(models.Station, id=id)
    return render(request, 'stations_detail.html', {'station': station})



############################# profile ########################################

@login_required
def profile(request):
  profile = models.Profile.objects.filter(user=request.user)
  if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data['username']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']
            password1 = user_form.cleaned_data['password1']
            password2 = user_form.cleaned_data['password2']
            phone = profile_form.cleaned_data['phone']
            address = profile_form.cleaned_data['address']
            user_photo = profile_form.cleaned_data['user_photo']
            about_me = profile_form.cleaned_data['about_me']
            profile_form = ProfileForm(phone=phone, address=address, user_photo=user_photo, about_me=about_me)
            user_form = UserForm(username=username, first_name=first_name, last_name=last_name, email=email, password1=password1, password2=password2)
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            context = {'profile': profile,'user_form': user_form,'profile_form': profile_form }
            return render(request, 'page-user.html', context)
        else:
            messages.error(request, _('Please correct the error below.'))
  else:
      user_form = UserForm(instance=request.user)
      profile_form = ProfileForm(instance=request.user.profile)

  context = {
  'profile': profile,
  'user_form': user_form,
  'profile_form': profile_form }
  return render(request, 'page-user.html', context)







    #nodes= models.Product.objects.filter(name__name='سوکت هالوژن')
    #nodes= models.Product.objects.filter(quantity=2)


##############################################################################
