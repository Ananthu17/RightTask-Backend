from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.main_class.as_view())
]