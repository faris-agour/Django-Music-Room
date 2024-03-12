from . import views
from django.urls import path

app_name = 'api'  # {% url 'api:index'%} used for this

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index')
]
