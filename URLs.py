from django.urls import path # type: ignore
from .views import add_item, search_item # type: ignore

urlpatterns = [
    path('add/', add_item, name='form'),
    path('search/', search_item, name='search'),
]

from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
