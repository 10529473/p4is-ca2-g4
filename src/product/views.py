from django.shortcuts import get_object_or_404, render
from .models import Product, Category

def print_product_list(request,category_id=None):
    """Product view with category filtering
    
    Keyword Arguments:
        category_id {int} -- category id for filtering (default: {None})
    """    
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        products = Product.objects.filter(category__pk=category_id)
    else:
        products = Product.objects.all()

    context = {
        'products':products,
        'categoryTree':Category.getTree(),
    }
    
    return render(request,"product/product.html",context)