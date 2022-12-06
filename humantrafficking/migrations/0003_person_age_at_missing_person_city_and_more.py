# Generated by Django 4.1.2 on 2022-12-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humantrafficking', '0002_alter_person_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age_at_missing',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='date_missing',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='race',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
