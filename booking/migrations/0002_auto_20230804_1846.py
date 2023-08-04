# Generated by Django 3.2.20 on 2023-08-04 18:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 18, 46, 22, 65767, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(choices=[('11:00:00', '11am'), ('11:30:00', '11:30am'), ('12:00:00', '12pm'), ('12:30:00', '12:30pm'), ('13:00:00', '1pm'), ('13:30:00', '1:30pm'), ('14:00:00', '2pm'), ('14:30:00', '2:30pm'), ('15:00:00', '3pm'), ('15:30:00', '3:30pm'), ('16:00:00', '4pm'), ('16:30:00', '4:30pm'), ('17:00:00', '5pm'), ('17:30:00', '5:30pm'), ('18:00:00', '6pm'), ('18:30:00', '6:30pm'), ('19:00:00', '7pm'), ('19:30:00', '7:30pm'), ('20:00:00', '8pm'), ('20:30:00', '8:30pm'), ('21:00:00', '9pm'), ('21:30:00', '9:30pm'), ('22:00:00', '10pm')], default=datetime.datetime(2023, 8, 4, 18, 46, 22, 65808, tzinfo=utc), max_length=10),
        ),
    ]
