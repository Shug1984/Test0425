from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        db_table = 'items'

    def __str__(self):
        return self.name
