from django.db import models


# Create your models here.
class Banks(models.Model):
    name = models.CharField(max_length=49)
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'banks'


class Branches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank = models.ForeignKey(Banks, models.CASCADE, related_name='bbranches')
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    class Meta:
        db_table = 'branches'