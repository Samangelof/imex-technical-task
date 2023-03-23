from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductsModel
from django.http import HttpResponse

def listening(request):
    template_name = 'gm.html'
    context = {
        'title': 'Listenings'
    }
    return render(request, template_name, context=context)


# -------------------------------------------------------------
# MVC
class MainHome(ListView):
    model = ProductsModel
    template_name: str = 'main.html'
    extra_context = {'title': 'Главная'}

# def main_home(request):
#     posts = ProductsModel.objects.all()
#     context = {
#         'menu': menu, 
#         'title': 'Главная',
#         }
#     return render(request, 'main.html', context=context)
# -------------------------------------------------------------


# -------------------------------------------------------------
class ProductsView(ListView):
    paginate_by = 6
    model = ProductsModel
    template_name: str = 'products.html'
    context_object_name: str = 'products'
    extra_context = {'title': 'Товары'}


def show_product(request, product_id):
    return HttpResponse(f"Отображение товара с id = {product_id}")
# -------------------------------------------------------------
