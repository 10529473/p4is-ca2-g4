from django.urls import path

from . import views

urlpatterns = [
    # ex: /product/
    path('', views.print_product_list, name='home'),
    path('<int:category_id>/', views.print_product_list, name='category'),
    
    # TODO: Make product list filter
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]