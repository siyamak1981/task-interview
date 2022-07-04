from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import User

class Product(models.Model):

    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()



class Rate(models.Model):

    product=models.ForeignKey(Product , on_delete=models.CASCADE, related_name='rate',null=True,blank=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE , related_name='rate', null=True,blank=True)
    ratenum=models.SmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],null=True,blank=True)

    def __str__(self):
        return str(self.ratenum)
