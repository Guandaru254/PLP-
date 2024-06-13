from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.

#def product_list(request, category_slug=None):
#   category = None
 #   categories = Category.objects.all()
  #  products = Product.objects.filter(available=True)
   # if category_slug:
    #    category = get_object_or_404(Category, slug=category_slug)
     #   products = products.filter(categories=category)
    #return render(request, 'techapp/product/list.html', {
     #   'category': category,
      #  'categories': categories,
       # 'products': products  
    #})
    
#def product_detail(request, id, slug):
 #   product = get_object_or_404(Product, id=id, slug=slug, available=True)
  #  return render(request, 'techapp/product/detail.html', {'product': product})

def index(request):
    context = {
        'question': 'What is the most widely used Python framework?',
        'option1': 'Django',
        'option2': 'Flask',
        'option3': 'Pyramid',
    }
    return render(request, 'index.html', context)

def form_view(request):
    if request.method == "POST":
       result = request.POST.get("answer")
       context = {"result": result }
       return render(request, "result.html", context)
    else:
        return render(request, 'index.html')
