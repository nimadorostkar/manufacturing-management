from django.urls import path, re_path
from app import views
#from .views import MapView

app_name='app'




urlpatterns = [
    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
    # other pages
    path('maps', views.maps, name='maps'),
    #path("maps", MapView.as_view()),
    path('profile', views.profile, name='profile'),
    path('search',views.search,name='search'),
    path('ticket',views.ticket,name='ticket'),
    # products
    path('products', views.products, name='products'),
    path('products_detail/<int:id>/',views.products_detail,name='products_detail'),
    # stations
    path('processes', views.processes, name='processes'),
    path('processes_detail/<int:id>/',views.processes_detail,name='processes_detail'),
    # orders
    path('order', views.order, name='order'),
    path('orders_detail/<int:id>/',views.orders_detail,name='orders_detail'),

    # add material, station, repository, transfer and product
    path('add_material', views.add_material, name='add_material'),
    path('add_station', views.add_station, name='add_station'),
    #path('add_repository', views.add_repository, name='add_repository'),
    #path('add_transfer', views.add_transfer, name='add_transfer'),
]
