# Generated by Django 4.0.6 on 2022-08-19 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrisur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='healthdrink',
            name='country',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='healthdrink',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='healthdrink',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='healthdrink',
            name='price',
            field=models.FloatField(),
        ),
    ]
