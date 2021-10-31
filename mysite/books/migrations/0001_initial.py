# Generated by Django 2.2 on 2021-10-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('rating', models.FloatField()),
                ('image', models.ImageField(default='images/non/noimg.jpg', upload_to='images')),
            ],
        ),
    ]
