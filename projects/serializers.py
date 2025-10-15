from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Project, ProjectImage

User = get_user_model()


class ProjectImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectImage
		fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
	images = ProjectImageSerializer(many=True, source="projectimage_set")
	class Meta:
		model = Project
		fields = "__all__"