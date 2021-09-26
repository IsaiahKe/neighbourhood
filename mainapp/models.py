from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    photo=CloudinaryField('image')
    neighbourhood=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,null=True)
    contact= PhoneNumberField(blank=True,null=True)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    admin=models.BooleanField(auto_created=False,null=True)
    
    
    @receiver(post_save,sender=User)
    def create_profile(sender,instance,created,**kwargs):
        try: 
          instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
    def __str__(self):
        return f'{User.username} Profile'
    
class Neighbourhood(models.Model):
    name= models.CharField(max_length=30,null=False)
    location=models.CharField(max_length=30,null=False)
    occupants=models.IntegerField(auto_created=0)
    
    def __str__(self):
        return self.name


class Business(models.Model):
    name=models.CharField(null=False,blank=False,max_length=30)
    category=models.CharField(null=False,max_length=30)
    residence=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE)    
    
