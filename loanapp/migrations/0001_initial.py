# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-23 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('dob', models.DateTimeField(null=True)),
                ('phone', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
