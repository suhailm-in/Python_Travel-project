from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    fblink=models.URLField()

    def __str__(self):
        return self.name

class Photoc(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name1