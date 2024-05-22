from rest_framework.generics import get_object_or_404
from retail.models import Dealer, Products
from rest_framework import generics
from retail.permissions import IsOwnerOrStaff
from retail.serializers import DealerSerializer, DealerCreateSerializer, ProductSerializer, DealerUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from users.models import User


class DealerCreateListAPIView(generics.ListCreateAPIView):
    """ Представление для создания и отображения списка экземпляров Dealer (Дилер) """
    queryset = Dealer.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DealerCreateSerializer
        else:
            return DealerSerializer

    # def perform_create(self, serializer):
    #     new_dealer = serializer.save()
    #     new_dealer.owner = get_object_or_404(User, id=self.request.user.id)
    #     new_dealer.save()

    def perform_create(self, serializer):
        new_dealer = serializer.save()
        new_dealer.owner = self.request.user
        new_dealer.save()


class DealerDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Представление для подробной информации, обновления и удаления экземпляра Dealer (Дилер) """
    queryset = Dealer.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return DealerUpdateSerializer
        else:
            return DealerSerializer


class ProductsCreateListAPIView(generics.ListCreateAPIView):
    """ Представление для создания и отображения списка экземпляров Products (Продукты) """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_product = serializer.save()
        new_product.owner = self.request.user
        new_product.save()


class ProductsDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Представление для подробной информации, обновления и удаления экземпляра Products (Продукты) """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]
