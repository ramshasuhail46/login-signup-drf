from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializer import UserLoginSerializer, UserRegisterSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

# Create your views here.


class UserRegistrationAPI(APIView):
    def get(self, request):
        return Response({"message": "register!"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'registeration successfull!', 'data': serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"serializer.data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPI(APIView):
    def get(self, request):
        return Response({"message": "login!"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            serializer.save()
            return Response({'message': 'login successfull!'}, serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"serializer.data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
