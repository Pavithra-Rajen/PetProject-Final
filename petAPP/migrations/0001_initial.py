# Generated by Django 4.2.2 on 2023-08-05 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='petstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('species', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
