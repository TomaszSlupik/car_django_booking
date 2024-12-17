from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer
from django.http import HttpResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib import messages  



class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            request.session["refresh"] = str(refresh)
            request.session["access"] = str(refresh.access_token)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "username": user.username 
            }, status=status.HTTP_200_OK)
        
        
        return Response({"error": "Niepoprawna nazwa użytkownika lub hasło."}, status=status.HTTP_400_BAD_REQUEST)


def error_login_view(request):
    return render(request, "error_login.html")


def come_back_to_main_page(request):
    return render(request, "login.html")


class RegisterView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():

            username = serializer.validated_data.get("username")
            if User.objects.filter(username=username).exists():
                 return render(request, "register.html", {"error": "Użytkownik już istnieje w bazie danych."})
            
            serializer.save()
            success_msg = "Zarejestrowałeś się pomyślnie!"
            messages.success(request, success_msg)
            return render(request, "register.html") 

        return render(request, "register.html", {"error": "Wystąpił błąd podczas rejestracji.", "form_errors": serializer.errors})
