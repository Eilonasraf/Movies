# Generated by Django 4.0.4 on 2022-04-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('discription', models.TextField(max_length=10000)),
                ('image', models.ImageField(upload_to='images/')),
                ('screen_shot', models.ImageField(upload_to='screenshots/')),
                ('movie_length', models.CharField(max_length=50)),
                ('release_date', models.DateTimeField()),
                ('movie_rate', models.CharField(max_length=100)),
                ('imdb_raiting', models.CharField(max_length=100)),
                ('movie_director', models.CharField(max_length=200)),
                ('movie_actor', models.CharField(max_length=1000)),
                ('movie_language', models.CharField(max_length=100)),
                ('movie_quality', models.CharField(max_length=100)),
                ('movie_size', models.CharField(max_length=100)),
                ('movie_suitable', models.CharField(max_length=100)),
                ('movie_link', models.TextField(max_length=10000)),
                ('movie_online', models.TextField(max_length=1000)),
                ('movie_type', models.CharField(max_length=700)),
                ('movie_subscription', models.CharField(max_length=700)),
                ('movie_category', models.CharField(max_length=100)),
            ],
        ),
    ]
