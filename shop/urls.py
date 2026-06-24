from django.urls import path
from .views import (ProductListView, category_list, products_detail_view,
                    search_products)

app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),  # Квадратные скобки!
    path('<slug:slug>/', category_list, name='category-list'),
    path('product/<int:id>/', products_detail_view, name='product_detail'),  # если нужно
    path('search/', search_products, name='search'),  # если нужно
]