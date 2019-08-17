from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    body =  models.TextField()
    image = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    url = models.TextField()
    comments = models.CharField(max_length=255)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def summary(self):
        return self.body[:165]  

    def __str__(self):
        return self.title

     