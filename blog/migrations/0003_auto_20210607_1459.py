# Generated by Django 3.1.7 on 2021-06-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210605_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='7.png', upload_to='media'),
        ),
    ]
