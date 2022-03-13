
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')
]