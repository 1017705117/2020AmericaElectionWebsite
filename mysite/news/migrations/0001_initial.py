# Generated by Django 3.1.3 on 2020-11-24 01:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=20, null=True)),
                ('content', models.TextField(null=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 11, 24, 9, 30, 13, 377921))),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 11, 24, 9, 30, 13, 378417))),
                ('content', models.CharField(max_length=100)),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
