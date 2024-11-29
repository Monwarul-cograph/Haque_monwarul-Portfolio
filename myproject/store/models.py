from django.db import models

# Create your models here.
class About(models.Model):
    説明文 = models.CharField(max_length=1000)
    職種 = models.CharField(max_length=100) 
    出身地 = models.CharField(max_length=500)
    所在地 = models.CharField(max_length=100)
    年齢 = models.IntegerField(default=25)
    学位 = models.CharField(max_length=100)
    メールアドレス = models.EmailField()


class Resume(models.Model):
    学士号メディアコミュニケーション学部情報文化学科 = models.CharField(max_length=2000)
    日本語学校 = models.CharField(max_length=2000)



class Social(models.Model):
    Linkedin_links = models.URLField(max_length = 1000)
    Line_links = models.URLField(max_length = 1000)

    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length= 100)
    message = models.CharField(max_length=1000)
    




