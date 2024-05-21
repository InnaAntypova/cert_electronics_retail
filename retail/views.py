from retail.models import Dealer, Products
from rest_framework import generics
from retail.serializers import DealerSerializer, DealerCreateSerializer, ProductSerializer, DealerUpdateSerializer


class DealerCreateListAPIView(generics.ListCreateAPIView):
    """ Представление для создания и отображения списка экземпляров Dealer (Дилер) """
    queryset = Dealer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DealerCreateSerializer
        else:
            return DealerSerializer


class DealerDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Представление для подробной информации, обновления и удаления экземпляра Dealer (Дилер) """
    queryset = Dealer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return DealerUpdateSerializer
        else:
            return DealerSerializer


class ProductsCreateListAPIView(generics.ListCreateAPIView):
    """ Представление для создания и отображения списка экземпляров Products (Продукты) """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductsDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Представление для подробной информации, обновления и удаления экземпляра Products (Продукты) """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
