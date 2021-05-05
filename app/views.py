from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from . import models
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, Ticket, Order, Process
from django.utils.translation import ugettext_lazy as _
from .forms import ProfileForm, UserForm, TicketForm, MaterialForm
from itertools import chain
from django.contrib.auth import get_user_model
from django.db import transaction
from django.urls import reverse
from django.views.generic.base import TemplateView




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
'''
class MapView(TemplateView):
    template_name = "ui-maps.html"
'''

@login_required()
def maps(request):
    maps= models.Process.objects.all()
    mapbox_access_token = 'pk.eyJ1IjoiZG9yb3N0a2FyIiwiYSI6ImNrbmVjdzg3djFkb3EycG8wZW5sdjNld3YifQ.AeDSXrxKTXAxPdIEESuPqA'
    return render(request, 'ui-maps.html', {
    'maps': maps,
    'mapbox_access_token': mapbox_access_token}
    )





################################# search #####################################

@login_required
def search(request):
    if request.method=="POST":
        search = request.POST['q']
        if search:
            process = models.Process.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
            product = models.Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
            match = chain(process, product)
            if match:
                return render(request,'search.html', {'sr': match})
            else:
                messages.error(request,  '   چیزی یافت نشد ، لطفا مجددا جستجو کنید ' )
        else:
            return HttpResponseRedirect('/search')
    return render(request, 'search.html', {})







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
def processes(request):
    processes= models.Process.objects.all()
    return render(request, 'processes.html', {'processes': processes})


@login_required()
def processes_detail(request, id):
    process = get_object_or_404(models.Process, id=id)
    processes= models.Process.objects.all()
    input = models.Tree.objects.filter(name=process)
    return render(request, 'processes_detail.html', {
    'process': process,
    'processes': processes,
    'input': input
    })



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





################################# ticket #####################################

@login_required()
@transaction.atomic
def ticket(request):
    send_tickets = models.Ticket.objects.filter(user=request.user).order_by('-created_on')
    received_tickets = models.Ticket.objects.filter(to=request.user).order_by('-created_on')
    ticket = chain(send_tickets, received_tickets)
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'POST':
        ticket_form=TicketForm(request.POST, request.FILES, instance=request.user)
        if ticket_form.is_valid():
            obj = Ticket() #gets new object
            obj.title = ticket_form.cleaned_data['title']
            obj.descriptions = ticket_form.cleaned_data['descriptions']
            obj.to = ticket_form.cleaned_data['to']
            obj.user = ticket_form.created_by=request.user
            obj.save()
            #messages.success(request, _('done successfully !'))
            context = {'ticket_form': ticket_form, 'ticket':ticket, 'users':users }
            return render(request, 'ticket.html', context)
        else:
            return HttpResponse("Form Failed to Validate")
    else:
      ticket_form=TicketForm(request.POST, request.FILES, instance=request.user)
      context = {'ticket_form': ticket_form, 'ticket':ticket, 'users':users }
      return render(request, 'ticket.html', context)






############################### manufacture ##################################

@login_required()
def order(request):
    orders = models.Order.objects.all()
    return render(request, 'order.html', {'orders': orders})




########################### manufacture_detail ###############################

@login_required()
def orders_detail(request, id):
    order = get_object_or_404(models.Order, id=id)
    orders = models.Order.objects.all()
    #manu_product = models.Product.objects.filter(name=manufacture.product.name)
    nodes = models.Tree.objects.filter(relatedProduct=order.product)
    #order_q = sum(product.price for product in cart_list)

    return render(request, 'orders_detail.html', {
    'orders': orders,
    'order': order,
    #'manu_product':manu_product,
    'nodes':nodes
    })







# ----------------------------------------------------------------------------
# add page for material, station, repository, transfer and product ...

@login_required()
def add_material(request):
    material = models.Process.objects.all()
    if request.method == 'POST':
          material_form = MaterialForm(request.POST, instance=request.user)
          if material_form.is_valid():
              obj = Process() #gets new object
              obj.name = material_form.cleaned_data['name']
              obj.position = material_form.cleaned_data['position']
              obj.description = material_form.cleaned_data['description']
              obj.inventory = material_form.cleaned_data['inventory']
              obj.min_inventory = material_form.cleaned_data['min_inventory']
              obj.manager = material_form.cleaned_data['manager']
              obj.supplier = material_form.cleaned_data['supplier']
              obj.save()
              messages.success(request, _('Your material was successfully added!'))
              context = {'material': material,'material_form': material_form }
              return render(request, 'add_material.html', context)
          else:
              messages.error(request, _('Please correct the error below.'))
    else:
        material_form = MaterialForm(request.POST)

    context = {'material': material,'material_form': material_form }
    return render(request, 'add_material.html', context)




@login_required()
def add_station(request):
    material = models.Process.objects.filter(user=request.user)
    if request.method == 'POST':
          material_form = MaterialForm(request.POST)
          if material_form.is_valid():
              name = user_form.cleaned_data['name']
              description = material_form.cleaned_data['description']
              inventory = material_form.cleaned_data['inventory']
              min_inventory = material_form.cleaned_data['min_inventory']
              manager = material_form.cleaned_data['manager']
              supplier = material_form.cleaned_data['supplier']
              material_form.save()
              messages.success(request, _('Your material was successfully added!'))
              context = {'material': material,'material_form': material_form }
              return render(request, 'page-user.html', context)
          else:
              messages.error(request, _('Please correct the error below.'))
    else:
        material_form = MaterialForm(request.POST)

    context = {'material': material,'material_form': material_form }
    return render(request, 'add_material.html', {'orders': orders})












    #nodes= models.Product.objects.filter(name__name='سوکت هالوژن')
    #nodes= models.Product.objects.filter(quantity=2)


##############################################################################
