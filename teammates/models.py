from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Teammate(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	stack = models.CharField(max_length=64, default="New")
	image = models.ImageField(upload_to="teammate_photos/", null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Teammate {self.first_name}"
	
	class Meta:
		verbose_name = "Teammate"
		verbose_name_plural = "Teammates"
		