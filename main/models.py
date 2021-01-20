from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100) 
    year = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
