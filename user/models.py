from django.contrib.auth.models import AbstractUser
from django.db import models

choices = [
    ("manager", "Manager"),
    ("backend", "BackEnd Dev"),
    ("frontend", "FrontEnd Dev"),
    ("designer", "Designer"),
    ("folder", "Folder"),
    ("other", "Other")
]

class User(AbstractUser):
	role = models.CharField(max_length=24, choices=choices, default="other")


