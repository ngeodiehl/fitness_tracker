# Generated by Django 2.1.2 on 2018-11-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessTracker_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fit_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='fitnessProfile',
        ),
    ]