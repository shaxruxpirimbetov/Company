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
from .models import Project
from .serializers import ProjectSerializer


class ProjectView(View):
	def get(self, request, project_id):
		project = Project.objects.filter(id=project_id).first()
		if not project:
			return render(request, "projects/project-404.html")
		project = ProjectSerializer(project).data
		return render(request, "projects/project-view.html", {"project": project})