# Generated by Django 4.1.2 on 2022-12-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humantrafficking', '0004_alter_person_age_at_missing_alter_person_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age_at_missing',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_missing',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='race',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
