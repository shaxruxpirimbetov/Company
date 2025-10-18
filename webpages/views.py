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
from .models import Page


class PageView(View):
	def get(self, request):
		page_id = request.GET.get("page_id")
		if not page_id:
			return HttpResponse("Not found")
		
		page = Page.objects.filter(id=page_id).first()
		if not page:
			return HttpResponse("Not found")
		return HttpResponse(page.html)