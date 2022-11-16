from django.db import models

# Create your models here.


class Person(models.Model):
    class Meta():
        db_table = "person"
