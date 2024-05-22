from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для отображения модели User (Пользователь) """
    class Meta:
        model = User
        fields = ['email', 'phone', 'city', 'telegram_id']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ Сериализатор для регистрации экземпляра User (Пользователь) """
    class Meta:
        model = User
        fields = ['email', 'password']
