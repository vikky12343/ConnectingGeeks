# Generated by Django 2.2.7 on 2019-11-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20191112_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
