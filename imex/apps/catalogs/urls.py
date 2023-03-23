from django.urls import path
from .views import MainHome, ProductsView, show_product, listening

urlpatterns = [
    # ------------------------------------------------
    # ...
    path('home/', listening, name='home'),
    path('', listening),
    path('products/', ProductsView.as_view()),
    path('products/<slug:product_id>/', show_product, name='products'),
]

