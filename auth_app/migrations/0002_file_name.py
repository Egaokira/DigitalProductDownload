# Generated by Django 3.2.16 on 2023-06-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.TextField(default=None, null=True),
        ),
    ]