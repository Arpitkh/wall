# Generated by Django 2.1b1 on 2018-07-21 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=250)),
                ('item_details', models.CharField(max_length=3000)),
                ('item_img', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
