from django.db import models
from django.conf import settings  

class Record(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,   
        on_delete=models.CASCADE,
        related_name='finance_records'
    )
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
