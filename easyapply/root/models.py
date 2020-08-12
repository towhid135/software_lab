from django.db import models
from django.db.models import Subquery
from datetime import datetime,date

class user(models.Model):
    userid = models.AutoField(primary_key=True,null=False,unique=True)
    field = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to=None, null=True, blank=True)
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


class PSC(models.Model):
    psc_id=models.AutoField(primary_key=True,null=False,unique=True)
    pschool=models.TextField()
    p_GPA=models.CharField(max_length=4)
    p_board=models.CharField(max_length=20)
    p_year=models.CharField(max_length=4)
    userid = models.ForeignKey(user, null=True ,on_delete=models.CASCADE)

class JSC(models.Model):
    jsc_id=models.AutoField(primary_key=True,null=False,unique=True)
    jschool=models.TextField()
    j_GPA=models.CharField(max_length=4)
    j_board=models.CharField(max_length=20)
    j_year=models.CharField(max_length=4)
    userid = models.ForeignKey(user, null=True, on_delete=models.CASCADE)

class SSC(models.Model):
    ssc_id=models.AutoField(primary_key=True,null=False,unique=True)
    sschool=models.TextField()
    s_group = models.CharField(max_length=10)
    s_GPA=models.CharField(max_length=4)
    s_board=models.CharField(max_length=20)
    s_year=models.CharField(max_length=4)

class HSC(models.Model):
    hsc_id=models.AutoField(primary_key=True,null=False,unique=True)
    hschool=models.TextField()
    h_group = models.CharField(max_length=10)
    h_GPA=models.CharField(max_length=4)
    h_board=models.CharField(max_length=20)
    h_year=models.CharField(max_length=4)
    userid = models.ForeignKey(user, null=True, on_delete=models.CASCADE)

class Honours(models.Model):
    ho_id=models.AutoField(primary_key=True,null=False,unique=True)
    ho_university=models.TextField()
    ho_program=models.CharField(max_length=4)
    ho_CGPA=models.CharField(max_length=4)
    ho_year=models.CharField(max_length=4)
    userid = models.ForeignKey(user, null=True, on_delete=models.CASCADE)

class Masters(models.Model):
    m_id=models.AutoField(primary_key=True,null=False,unique=True)
    m_university=models.TextField()
    m_program=models.CharField(max_length=4)
    m_CGPA=models.CharField(max_length=4)
    m_year=models.CharField(max_length=4)
    userid = models.ForeignKey(user, null=True, on_delete=models.CASCADE)

class PHD(models.Model):
    phd_id=models.AutoField(primary_key=True,null=False,unique=True)
    uni=models.TextField()
    field=models.TextField()
    phd_year=models.CharField(max_length=4)
    userid = models.ForeignKey(user, null=True, on_delete=models.CASCADE)

class Academic(models.Model):
    a_id = models.AutoField(primary_key=True, null=False, unique=True)
    psc_id = models.ForeignKey(PSC, on_delete=models.CASCADE,null =True,blank=True)
    jsc_id = models.ForeignKey(JSC, on_delete=models.CASCADE,null =True,blank=True)
    ssc_id= models.ForeignKey(SSC, on_delete=models.CASCADE,null =True,blank=True)
    hsc_id = models.ForeignKey(HSC, on_delete=models.CASCADE, null=True, blank=True)
    ho_id  = models.ForeignKey(Honours, on_delete=models.CASCADE,null =True,blank=True)
    m_id   = models.ForeignKey(Masters, on_delete=models.CASCADE,null =True,blank=True)
    phd_id = models.ForeignKey(PHD, on_delete=models.CASCADE,null =True,blank=True)
