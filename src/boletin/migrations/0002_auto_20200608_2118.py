# Generated by Django 3.0.7 on 2020-06-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrado',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
