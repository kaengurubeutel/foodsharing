# Generated by Django 3.2.9 on 2022-02-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='hometown',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='Bielefeld', max_length=20, verbose_name='email'),
        ),
    ]
