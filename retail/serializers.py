from rest_framework import serializers
from retail.models import Contacts, Products, Dealer


class ContactsSerializer(serializers.ModelSerializer):
    """ Сериализатор для отображения полей модели Contacts (Контакты) """

    class Meta:
        model = Contacts
        fields = ['email', 'country', 'city', 'street', 'house_number']


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для отображения полей модели Products (Продукты) """

    class Meta:
        model = Products
        fields = ['title', 'model', 'product_release_date', 'price', 'quantity']


class DealerSerializer(serializers.ModelSerializer):
    """ Сериализатор для отображения полей модели Dealer (Дилер) """

    class Meta:
        model = Dealer
        fields = ['title', 'contacts', 'products', 'shipper', 'debt', 'created', 'dealer_type', 'level']


class DealerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['title', 'contacts', 'products', 'shipper', 'dealer_type']