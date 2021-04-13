from django.urls import path, re_path
from app import views

app_name='app'




urlpatterns = [
    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
    path('maps', views.maps, name='maps'),
    path('product', views.product, name='product'),
    path('products_detail/<int:id>/',views.products_detail,name='products_detail'),
]
