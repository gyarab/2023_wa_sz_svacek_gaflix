
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('filmy.urls'), name='filmy'),
    #path('', TemplateView.as_view(template_name='filmy/prvni.html'), name='home'),
    #path('druha/', TemplateView.as_view(template_name='filmy/druha.html'), name='druha'),
]
