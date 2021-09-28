from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User, UserManager
from cloudinary.models import CloudinaryField
from django.db.models import fields
from django.db.models.fields import DateField
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .email import send_welcome_email
from mainapp import email
# Create your models here.
class Profile(models.Model):
    photo=CloudinaryField('image')
    hood=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,null=True)
    contact=PhoneNumberField(blank=True)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,blank=True)
    admin=models.BooleanField(auto_created=True,null=False,default=False,)
    
    @receiver(post_save,sender=User)
    def create_profile(sender,instance,**kwargs):
        try: 
          instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            #add email function after  registration
    def __str__(self):
        return f'{self.user}'
    
   

    
class Neighbourhood(models.Model):
    name= models.CharField(max_length=30,null=False)
    location=models.CharField(max_length=30,null=False)
    occupants=models.IntegerField(auto_created=0)
    
    def __str__(self):
        return self.name
    def addhood(self):
        return self.save()
    def deletehood(self):
        self.delete()
    @classmethod
    def findhood(cls,name):
        for i in cls:
            if cls.name==name:
                return cls
            return False


class Business(models.Model):
    name=models.CharField(null=False,blank=False,max_length=30)
    email=models.EmailField(null=True)
    contact=PhoneNumberField(null=True)
    location=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name
    def addbusiness(self):
        self.save()
        
    def removebusiness(self):
        self.delete() 
        
    
class Alert(models.Model):
    content=models.TextField(null=False,blank=True)
    image=CloudinaryField('image',null=True)
    author=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    hood=models.ForeignKey('Neighbourhood',null=True,blank=True,on_delete=models.CASCADE)
    posted=models.DateField(auto_now=timezone.now)
    
    
    def __str__(self):
        return f'{self.author.username}'
    
class Category(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    email=models.EmailField(null=True)
    contact=PhoneNumberField(null=True)
    location=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
    
    
