from django.db import models
from django.db.models import Subquery
from datetime import datetime,date

class user(models.Model):
    userid = models.AutoField(primary_key=True,null=False,unique=True)
    field = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    achievement = models.TextField()
    objective = models.TextField()
    exp = models.TextField()

class skill(models.Model):
    soft = models.TextField()
    technical = models.TextField()
    organizational = models.TextField()
    computer = models.TextField()
    language = models.TextField()
    userid = models.ForeignKey(user,on_delete=models.CASCADE)


class employer(models.Model):
    e_id = models.AutoField(primary_key=True,null=False,unique=True)
    company_name = models.CharField(max_length=200)
    company_address=models.TextField()


class circular(models.Model):
    circular_id = models.AutoField(primary_key=True, null=False, unique=True)
    e_id = models.ForeignKey(employer,null=True, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    salary = models.CharField(max_length=30)
    requirements = models.TextField()
    date = models.CharField(max_length=30)



