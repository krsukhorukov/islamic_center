from django.db import models
from django.contrib.auth.models import User

class MainNews(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.title


class MainNewsEn(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.title


class MainNewsUz(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.title


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    date = models.DateField()
    image = models.TextField()
    video = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.title



class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    phone_number_personal = models.CharField(max_length=1000)
    phone_number_work = models.CharField(max_length=1000)
    marital_status = models.CharField(max_length=1000)
    number_of_children = models.CharField(max_length=1000)
    residental_status = models.CharField(max_length=1000)
    type_of_work = models.CharField(max_length=1000)
    type_of_membership = models.CharField(max_length=1000)
    donation_amount = models.IntegerField()
    donation_frequency = models.CharField(max_length=1000)
    donation_date =models.DateField()
    