# Generated by Django 2.2.1 on 2019-06-23 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190623_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(default='download.svg', upload_to='upload/'),
        ),
    ]
