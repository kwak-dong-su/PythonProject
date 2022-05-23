from django.db import models

# Create your models here.

class product(models.Model):
    no=models.IntegerField(100)
    name=models.CharField(max_length=500)
    price=models.IntegerField(100)
    company=models.CharField(max_length=500)

    def __str__(self):
        return str(self.no)+', '+self.name+', '+str(self.price)+', '+self.company