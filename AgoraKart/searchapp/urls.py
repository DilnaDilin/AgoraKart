
from . import views
from django.urls import path
app_name='searchapp'
urlpatterns = [

    path('',views.searchProd,name='searchProd'),


]