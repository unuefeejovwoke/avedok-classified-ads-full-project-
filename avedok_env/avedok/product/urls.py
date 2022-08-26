from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_advertise', views.add_advertise,name='add_advertise'),
    path('update-ads/<slug:ads_slug>/', views.updateAds, name='update-ads'),
    path('all_products', views.productList, name='product_list'),
    path('<slug:category_slug>', views.productList, name='product_list_cateogry'),
    path('detail/<slug:product_slug>', views.productDetail, name='product_detail'),
]

handler404 = 'product.views.custom_page_not_found_view'