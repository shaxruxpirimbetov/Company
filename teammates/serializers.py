from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Teammate

User = get_user_model()


class TeammateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teammate
		fields = "__all__"