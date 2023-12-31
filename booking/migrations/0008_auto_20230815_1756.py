# Generated by Django 3.2.20 on 2023-08-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20230814_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
