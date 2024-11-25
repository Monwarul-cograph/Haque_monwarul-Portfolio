from django.db import models

# Create your models here.
class About(models.Model):
    discription = models.CharField(max_length=1000)
    designation = models.CharField(max_length=100) 
    short_description = models.CharField(max_length=500)
    birth = models.DateField()
    website_link = models.URLField(max_length=1000)
    phone = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    age = models.IntegerField(max_length=10)
    degree = models.CharField(max_length=100)
    email = models.EmailField()


class Social(models.Model):
    Linkedin_links = models.URLField(max_length = 1000)
    Line_links = models.URLField(max_length = 1000)

    


