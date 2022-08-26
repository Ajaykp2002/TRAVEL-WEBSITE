from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="photos")
    description=models.TextField()
    def __str__(self):
        return self.name
class Team(models.Model):
    name=models.CharField(max_length=100)
    img = models.ImageField(upload_to="photo")
    description = models.TextField()
    def __str__(self):
        return self.name