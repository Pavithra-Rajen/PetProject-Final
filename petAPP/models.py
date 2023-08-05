from django.db import models
from django.urls import reverse

# Create your models here.
class petstore(models.Model):
    gender=(('male','male'),('female','female'))
    # image=models.ImageField(upload_to="media")
    image=models.ImageField(null=True,blank=True)
    species=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    breed=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    price=models.IntegerField()




    def get_absolute_url(self):
        return reverse('list')
        # return reverse('details',kwargs={'pk':self.pk})
    