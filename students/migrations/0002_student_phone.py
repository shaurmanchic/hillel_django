# Generated by Django 3.2.5 on 2021-08-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
