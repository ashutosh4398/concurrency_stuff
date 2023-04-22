import datetime
from django.db import models

# Create your models here.
class Companies(models.Model):
    symbol = models.CharField(max_length=64, null=False)
    price = models.FloatField(default=0)
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self) -> str:
        return f"{self.id} -> {self.symbol}"