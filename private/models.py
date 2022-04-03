from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewRegister(models.Model):
    fullname = models.CharField(max_length=100)
    voterid = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    edit = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.voterid