# Generated by Django 2.2.4 on 2019-08-16 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_online', models.DateTimeField(auto_now_add=True)),
                ('followers', models.ManyToManyField(related_name='followers1', to='twitter_clone.TwitterUser')),
                ('following', models.ManyToManyField(related_name='following1', to='twitter_clone.TwitterUser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='twitter_clone.TwitterUser')),
                ('likes', models.ManyToManyField(to='twitter_clone.TwitterUser')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('new_followers', models.ManyToManyField(to='twitter_clone.TwitterUser')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='twitter_clone.TwitterUser')),
            ],
        ),
    ]
