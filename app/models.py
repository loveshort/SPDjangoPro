from django.db import models

# Create your models here.
class AppModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

