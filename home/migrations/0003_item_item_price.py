# Generated by Django 2.1b1 on 2018-07-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180721_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]