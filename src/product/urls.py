from django.urls import path

from . import views

urlpatterns = [
    # ex: /product/
    path('', views.print_product_list, name='home'),
    path('<int:category_id>/', views.print_product_list, name='category'),
]