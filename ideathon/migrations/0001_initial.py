# Generated by Django 3.2.3 on 2021-05-17 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('hi-sw', 'hi-sw'), ('club', 'club')], max_length=300)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('mediafile', models.FileField(upload_to='mediafiles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
