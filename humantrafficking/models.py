from django.db import models

# Create your models here.


class Person(models.Model):
    date_missing = models.DateField()
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    age_at_missing = models.IntegerField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)

    def __str__(self):
        return self.last_name

    class Meta():
        db_table = "persons"
