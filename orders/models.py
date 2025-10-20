from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=32)
	description = models.TextField()
	phone = models.CharField(max_length=20)
	status = models.CharField(max_length=20, default="Active")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Order {self.title}"
	
	class Meta:
		verbose_name = "Order"
		verbose_name_plural = "Orders"

		

