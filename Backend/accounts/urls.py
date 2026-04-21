from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Этот эндпоинт сам проверит логин/пароль и выдаст токены
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Эндпоинт для обновления токена
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]