from django.db import models

# Create your models here.
class review(models.Model):
    review_place_name=models.CharField(max_length=500)
    review_pos_neg=models.IntegerField()
    review_content=models.CharField(max_length=500)
    review_writer=models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)+', '+self.review_place_name+', '+str(self.review_pos_neg)+', '+self.review_content+', '+self.review_writer
