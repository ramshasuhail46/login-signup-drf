from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializer import UserLoginSerializer, UserRegisterSerializer, EmailVerificationSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

import random
from django.conf import settings
from django.core.mail import send_mail

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


class EmailVerifyAPI(APIView):
    def get(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        if serializer.is_valid():

            subject = 'Account Verification Email'
            otp = random.randint(0000, 9999)
            message = 'OTP: ' + str(otp)
            email_to = serializer.validated_data['email']
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [email_to])

            user = User.objects.get(email=email_to)
            user.otp = otp
            user.save()

            return Response({"message": "verification email sent!"}, status=status.HTTP_200_OK)
        return Response({"serializer.data": serializer.errors}, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            user = User.objects.get(email=email)
            if user.otp == otp:
                user.is_active = True
                user.save()
                return Response({"message": 'Email Verified'}, status=status.HTTP_202_ACCEPTED)
            return Response({"message": 'Invalid OTP'}, status=status.HTTP_202_ACCEPTED)
        return Response({"serializer.data": serializer.errors}, status=status.HTTP_202_ACCEPTED)
