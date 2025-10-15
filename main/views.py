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
from projects.models import Project
from projects.serializers import ProjectSerializer
from teammates.models import Teammate
from teammates.serializers import TeammateSerializer

User = get_user_model()


class HomeView(View):
	def get(self, request):
		projects = Project.objects.all()
		teammates = Teammate.objects.all()
		projects = ProjectSerializer(projects, many=True).data
		teammates = TeammateSerializer(teammates, many=True).data
		return render(request, "index.html", {"projects": projects, "teammates": teammates})

