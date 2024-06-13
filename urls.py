from django.urls import path
from . import views
from .views import form_view, index 

app_name = 'techapp'

urlpatterns = [
    path('', views.index, name='home'),
    path("result/", form_view, name='form_view'), 
]
