from django.db import models


class Project(models.Model):
	title = models.CharField(max_length=24)
	description = models.TextField()
	logo = models.ImageField(upload_to="project_logos/")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Project {self.title}"
	
	class Meta:
		verbose_name = "Project"
		verbose_name_plural = "Projects"


class ProjectImage(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="project_images/")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Image for {self.project.title}"
	
	class Meta:
		verbose_name = "Project Image"
		verbose_name_plural = "Project Images"
		

