from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Teammate
from .serializers import TeammateSerializer


class TeammateView(View):
	def get(self, request, teammate_id):
		teammate = Teammate.objects.filter(id=teammate_id).first()
		if not teammate:
			return render(request, "teammates/teammate-404.html")
		teammate = TeammateSerializer(teammate).data
		return render(request, "teammates/teammate-view.html", {"teammate": teammate})
	