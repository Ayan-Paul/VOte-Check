from django.contrib.auth.models import User
from django.db import models

class UserExtra(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='private/images/',null=True);
    booth_no = models.IntegerField(blank=True,null=True)
    telephone = models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return self.user