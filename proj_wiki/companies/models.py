import datetime
from django.db import models

# Create your models here.
class Companies(models.Model):
    symbol = models.CharField(max_length=64, null=False)
    price = models.FloatField(default=0)
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)
    # private field to keep track of number of updates
    # no need to specify it any where, as we will be updating it on every save call
    _update_count = models.IntegerField(default=0, verbose_name="update_count", db_column="update_count")

    def __str__(self) -> str:
        return f"{self.id} -> {self.symbol}"
    
    def save(self, *args, **kwargs) -> None:
        print("Saving")
        self._update_count += 1
        return super().save(*args, **kwargs)