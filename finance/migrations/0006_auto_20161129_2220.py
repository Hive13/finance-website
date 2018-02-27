# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20161128_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2009, b'2009'), (2010, b'2010'), (2011, b'2011'), (2012, b'2012'), (2013, b'2013'), (2014, b'2014'), (2015, b'2015'), (2016, b'2016'), (2017, b'2017')], default=2016)),
                ('month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=11)),
                ('members_cornerstone', models.IntegerField(default=0)),
                ('members_full', models.IntegerField(default=0)),
                ('members_fullwarden', models.IntegerField(default=0)),
                ('members_student', models.IntegerField(default=0)),
                ('members_studentwarden', models.IntegerField(default=0)),
                ('pnc_beginning', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pnc_deposits', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pnc_deductions', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pnc_ending', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pp_beginning', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pp_credits', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pp_fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pp_payments', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pp_transfers', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('pp_ending', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('otherincome', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('laserincome', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('otherexpense', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('rent', models.DecimalField(decimal_places=2, default=1150.0, max_digits=9)),
                ('cable', models.DecimalField(decimal_places=2, default=64.15, max_digits=9)),
                ('insurance', models.DecimalField(decimal_places=2, default=59.51, max_digits=9)),
            ],
            options={
                'get_latest_by': 'pk',
            },
        ),
        migrations.DeleteModel(
            name='MonthlySummary',
        ),
    ]
