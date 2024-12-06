from django.urls import path
from . import views

urlpatterns = [
    path('get_form/', views.validate_form, name='get_form'),
]