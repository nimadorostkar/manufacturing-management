from django.urls import path, re_path
from app import views

app_name='app'




urlpatterns = [
    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
    # other pages
    path('maps', views.maps, name='maps'),
    path('profile', views.profile, name='profile'),
    path('search',views.search,name='search'),
    # products
    path('products', views.products, name='products'),
    path('products_detail/<int:id>/',views.products_detail,name='products_detail'),
    # stations
    path('stations', views.stations, name='stations'),
    path('stations_detail/<int:id>/',views.stations_detail,name='stations_detail'),
]
