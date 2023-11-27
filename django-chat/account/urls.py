from django.urls import path
from .views import UserCreateView, UserLoginView

urlpatterns = [
	path('register/', UserCreateView.as_view(), name='register'),
	path('login/', UserLoginView.as_view(), name='login'),
]