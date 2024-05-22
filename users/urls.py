from django.urls import path
from users.apps import UsersConfig
from users.views import UserRegistrationAPIView, UserDetailUpdateDeleteAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('<int:pk>/', UserDetailUpdateDeleteAPIView.as_view(), name='user_detail_update_delete'),
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
