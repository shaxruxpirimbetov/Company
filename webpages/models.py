from django.db import models


class Page(models.Model):
	title = models.CharField(max_length=24)
	html = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Page {self.title}"
	
	class Meta:
		verbose_name = "Page"
		verbose_name_plural = "Pages"
		