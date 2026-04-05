
from django.db import models
from django.conf import settings

class Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    amount = models.FloatField()
    type = models.CharField(max_length=10)
