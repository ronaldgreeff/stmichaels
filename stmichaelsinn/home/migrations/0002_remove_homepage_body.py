# Generated by Django 3.0.5 on 2020-05-05 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
    ]
