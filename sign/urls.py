from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.add, name='add'),
    path('add/', views.added, name='added'),
]

