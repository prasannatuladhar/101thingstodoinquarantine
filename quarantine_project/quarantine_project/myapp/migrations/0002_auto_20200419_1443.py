# Generated by Django 2.2 on 2020-04-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatdo',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
