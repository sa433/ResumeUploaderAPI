from django.db import models

STATE_CHOICES = ((
    ('Maharashtra', 'Maharashtra'),
    ('Kerala', 'Kerala'),
    ('Bihar', 'Bihar')
))

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField(auto_now_add=False, auto_now=False)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to="myimage", blank=True)
    pfile = models.FileField(upload_to="myfile", blank=True)