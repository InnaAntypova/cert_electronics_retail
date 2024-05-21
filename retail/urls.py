from django.urls import path
from retail.apps import RetailConfig
from retail.views import DealerCreateListAPIView, DealerDetailUpdateDeleteAPIView, ProductsCreateListAPIView, \
    ProductsDetailUpdateDeleteAPIView

app_name = RetailConfig.name

urlpatterns = [
    path('', DealerCreateListAPIView.as_view(), name='create&list_dealers'),
    path('<int:pk>/', DealerDetailUpdateDeleteAPIView.as_view(), name='detail/update/delete_dealers'),
    path('products/', ProductsCreateListAPIView.as_view(), name='create&list_products'),
    path('products/<int:pk>/', ProductsDetailUpdateDeleteAPIView.as_view(), name='detail/update/delete_products')
]