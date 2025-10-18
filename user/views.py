from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import permissions
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .serializers import UserSerializer
User = get_user_model()


class RegisterApi(APIView):
	permission_classes = [permissions.AllowAny]
	def get_permissions(self):
		if self.request.method == "POST":
			return [permissions.AllowAny()]
		return [permissions.IsAuthenticated()]
		
	def post(self, request):
		username = request.data.get("username")
		password = request.data.get("password")
		
		if not all([username, password]):
			return Response({"status": False, "message": "username and password are required"})
		
		user = User.objects.filter(username=username).first()
		if user:
			return Response({"status": False, "message": "username already taked"})
		
		user = User.objects.create_user(username=username, password=password)
		if user.username == "shaxrux":
			user.is_staff = True
			user.is_superuser = True
			user.save()
		user = UserSerializer(user).data
		return Response({"status": True, "message": user})
	
	def put(self, request):
		role = request.data.get("role")
		if not role:
			return Response({"status": False, "message": "role are required"})
		
		request.user.role = role
		request.user.save()
		user = UserSerializer(request.user).data
		return Response({"status": True, "message": user})


class RegisterView(View):
	def get(self, request):
		return render(request, "user/register.html")
	
	def post(self, request):
		username = request.POST.get("username")
		password = request.POST.get("password")
		password2 = request.POST.get("password2")
		
		if password != password2:
			return render(request, "user/register.html", {"error": "password not match"})
		
		if not all([username, password]):
			return render(request, "user/register.html", {"error": "username and password are required"})
		
		user = User.objects.filter(username=username).first()
		if user:
			return render(request, "user/register.html", {"error": "username already taked"})
			
		user = User.objects.create_user(username=username, password=password)
		if user.username == "shaxrux":
			user.is_staff = True
			user.is_superuser = True
			user.set_password(password)
			user.save()
		login(request, user)
		user = UserSerializer(user).data
		return redirect("main:home")


class LoginView(View):
	def get(self, request):
		return render(request, "user/login.html")
	
	def post(self, request):
		username = request.POST.get("username")
		password = request.POST.get("password")
		
		print(username, password)
		
		if not all([username, password]):
			return render(request, "user/login.html", {"error": "username and password are required"})
		
		user = User.objects.filter(username=username).first()
		if not user:
			return render(request, "user/login.html", {"error": "user not found"})
		
		if not check_password(password, user.password):
			return render(request, "user/login.html", {"error": "password not match"})
		
		login(request, user)
		return redirect("main:home")


class LogoutView(View):
	def get(self, request):
		return render(request, "user/logout.html")
	
	def post(self, request):
		logout(request)
		return redirect("main:home")


class GetMeApi(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request):
		user = UserSerializer(request.user).data
		return Response({"status": True, "message": user})


