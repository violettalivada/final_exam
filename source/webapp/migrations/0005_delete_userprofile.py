# Generated by Django 2.2 on 2021-01-23 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_userprofile_friends'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]