from django.urls import path

from api.views import UserRegistrationAPI, UserLoginAPI

urlpatterns = [
    path('register/', UserRegistrationAPI.as_view(), name='register'),
    path('login/', UserLoginAPI.as_view(), name='login')

]
