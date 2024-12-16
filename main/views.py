from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from rest_framework import serializers
from django.contrib.auth import authenticate



# Create your views here.
def main_view(request):
    return render(request, "main.html")

