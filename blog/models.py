from django.db import models
from django.core.exceptions import ValidationError
from autoslug import AutoSlugField 
from django.contrib.auth.models import User
from django.conf import settings 
from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.
class post(models.Model):
    Sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    desc=models.TextField()
    time=models.DateTimeField(blank=True,auto_now=True)
    
    

    thumbnail=models.ImageField( upload_to='media')



    def _str_(self):
        return self.title


class contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    issue = models.TextField()

    def __str__(self):
        return self.Name


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField( upload_to='media',default='7.png')
    
    
    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User) #add this
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)

@receiver(post_save, sender=User) #add this
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    






