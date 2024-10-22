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
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK)


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
            serializer.save()
            return redirect("login")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
