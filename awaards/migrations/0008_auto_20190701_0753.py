# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-01 04:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awaards', '0007_profile_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('usability_rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('design_rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('content_rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awaards.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='contentrating',
            name='post',
        ),
        migrations.RemoveField(
            model_name='contentrating',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='designrating',
            name='post',
        ),
        migrations.RemoveField(
            model_name='designrating',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='usabilityrating',
            name='post',
        ),
        migrations.RemoveField(
            model_name='usabilityrating',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='ContentRating',
        ),
        migrations.DeleteModel(
            name='DesignRating',
        ),
        migrations.DeleteModel(
            name='UsabilityRating',
        ),
    ]
