from rest_framework import serializers
from retail.models import Products, Dealer


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для отображения полей модели Products (Продукты) """

    class Meta:
        model = Products
        fields = ['title', 'model', 'product_release_date', 'price', 'quantity', 'owner']


class DealerSerializer(serializers.ModelSerializer):
    """ Сериализатор для отображения полей модели Dealer (Дилер) """
    products = ProductSerializer(many=True)

    class Meta:
        model = Dealer
        fields = ['title', 'dealer_type', 'email', 'country', 'city', 'street', 'house_number', 'products', 'shipper',
                  'debt', 'created', 'level']
        read_only_fields = ['level', 'debt']


class DealerCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания экземпляра модели Dealer (Дилер) """
    class Meta:
        model = Dealer
        fields = ['title', 'dealer_type', 'email', 'country', 'city', 'street', 'house_number', 'shipper', 'owner']


class DealerUpdateSerializer(serializers.ModelSerializer):
    """ Сериализатор для обновления Dealer (Дилер) """
    class Meta:
        model = Dealer
        fields = ['title', 'dealer_type', 'email', 'country', 'city', 'street', 'house_number', 'products', 'shipper']
        read_only_fields = ['level', 'debt']
