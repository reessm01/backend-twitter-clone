# Generated by Django 2.2.4 on 2019-08-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_clone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='mentions',
            field=models.ManyToManyField(to='twitter_clone.Tweet'),
        ),
    ]