# Generated by Django 5.1 on 2024-08-31 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]