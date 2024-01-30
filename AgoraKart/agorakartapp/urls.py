
from . import views
from django.urls import path
app_name='agorakartapp'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='all_product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdDetail,name='productDetail')

]