from django.contrib import admin
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from catalogo.views import indexView


urlpatterns = [
    path('', RedirectView.as_view(url='catalogo/',permanent=True)),
    path('catalogo/', indexView, name='index') 
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
