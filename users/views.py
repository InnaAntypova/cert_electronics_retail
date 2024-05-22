from rest_framework import generics, status
from rest_framework.response import Response
from users.permissions import IsOwnerOrStaff
from users.models import User
from users.serializers import UserRegistrationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserRegistrationAPIView(generics.CreateAPIView):
    """ Представление для регистрации нового User (Пользователя) """
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            password = serializer.validated_data['password']
            user.set_password(password)  # зашифровать пароль
            user.is_active = True  # активировать пользователя
            user.save()
            context = {'email': user.email, 'password': password}
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            user = User.objects.get(email=serializer.data['email'])
            if user:
                return Response({'message': 'Такой пользователь уже существует.'})


class UserDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Представление для получения подробной информации, обновления и удаления экземпляра User (Пользователь) """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]
