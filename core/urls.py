from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    #path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls"))  # add this
]
