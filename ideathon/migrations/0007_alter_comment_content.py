# Generated by Django 3.2.3 on 2021-05-21 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideathon', '0006_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
    ]