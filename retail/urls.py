from django.urls import path
from retail.apps import RetailConfig
from retail.views import DealerCreateListAPIView

app_name = RetailConfig.name

urlpatterns = [
    path('', DealerCreateListAPIView.as_view(), name='create and list dealers')
]