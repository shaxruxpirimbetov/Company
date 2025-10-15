from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponse
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


class GetMeApi(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request):
		user = UserSerializer(request.user).data
		return Response({"status": True, "message": user})


