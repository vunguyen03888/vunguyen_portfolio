# Generated by Django 2.2.8 on 2021-04-23 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='aboutus',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='references',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
