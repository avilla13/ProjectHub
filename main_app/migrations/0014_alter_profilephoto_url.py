# Generated by Django 4.2.3 on 2023-08-07 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_profilephoto_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilephoto',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]