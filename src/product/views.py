from django.shortcuts import get_object_or_404, render
from .models import Product, Category

def print_product_list(request,category_id=None):
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


# TODO: Build products tree view
def tree_view(request):
    people = Person.objects.prefetch('children')
    return render(request, 'template.html', {'people': people})


# TODO: Build products filter
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)