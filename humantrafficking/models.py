from django.db import models

# Create your models here.


class Person(models.Model):
    def Meta():
        db_table = "person"
