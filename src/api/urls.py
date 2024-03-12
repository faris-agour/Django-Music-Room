from django.urls import path

from .views import RoomView

app_name = 'api'  # {% url 'api:index'%} used for this

urlpatterns = [
    path('', RoomView.as_view()),
    path('home/', RoomView.as_view())
]
