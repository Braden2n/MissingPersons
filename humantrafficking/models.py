from django.db import models

# Create your models here.


class Person(models.Model):
    date_missing = models.DateField(null=True)
    last_name = models.CharField(max_length=45, null=True)
    first_name = models.CharField(max_length=45, null=True)
    age_at_missing = models.IntegerField(null=True)
    city = models.CharField(max_length=45, null=True)
    state = models.CharField(max_length=2, null=True)
    gender = models.CharField(max_length=1, null=True)
    race = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.last_name

    class Meta():
        db_table = "persons"
