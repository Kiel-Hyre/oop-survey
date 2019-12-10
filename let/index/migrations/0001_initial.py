# Generated by Django 2.2.2 on 2019-12-09 11:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Only Alphabets are allowed', regex='^[a-zA-Z ]*$')])),
                ('f1', models.IntegerField(verbose_name='Personal Factor 1')),
                ('f2', models.IntegerField(verbose_name='Personal Factor 2')),
                ('f3', models.IntegerField(verbose_name='Personal Factor 3')),
                ('f4', models.IntegerField(verbose_name='Personal Factor 4')),
                ('f5', models.IntegerField(verbose_name='Personal Factor 5')),
                ('f6', models.IntegerField(verbose_name='Family Factor 1')),
                ('f7', models.IntegerField(verbose_name='Family Factor 2')),
                ('f8', models.IntegerField(verbose_name='Family Factor 3')),
                ('f9', models.IntegerField(verbose_name='Family Factor 4')),
                ('f10', models.IntegerField(verbose_name='Family Factor 5')),
                ('f11', models.IntegerField(verbose_name='Peer Factor 1')),
                ('f12', models.IntegerField(verbose_name='Peer Factor 2')),
                ('f13', models.IntegerField(verbose_name='Peer Factor 3')),
                ('f14', models.IntegerField(verbose_name='Peer Factor 4')),
                ('f15', models.IntegerField(verbose_name='Peer Factor 5')),
                ('f16', models.IntegerField(verbose_name='School Factor 1')),
                ('f17', models.IntegerField(verbose_name='School Factor 2')),
                ('f18', models.IntegerField(verbose_name='School Factor 3')),
                ('f19', models.IntegerField(verbose_name='School Factor 4')),
                ('f20', models.IntegerField(verbose_name='School Factor 5')),
                ('f21', models.IntegerField(verbose_name='School Factor 1')),
                ('f22', models.IntegerField(verbose_name='School Factor 2')),
                ('f23', models.IntegerField(verbose_name='School Factor 3')),
                ('f24', models.IntegerField(verbose_name='School Factor 4')),
                ('f25', models.IntegerField(verbose_name='School Factor 5')),
                ('total', models.IntegerField(default=0, null=True, verbose_name='Total')),
                ('over', models.IntegerField(default=0, null=True, verbose_name='Average')),
                ('o1', models.IntegerField(default=0, null=True, verbose_name='Overall 1')),
                ('o2', models.IntegerField(default=0, null=True, verbose_name='Overall 2')),
                ('o3', models.IntegerField(default=0, null=True, verbose_name='Overall 3')),
                ('o4', models.IntegerField(default=0, null=True, verbose_name='Overall 4')),
                ('o5', models.IntegerField(default=0, null=True, verbose_name='Overall 5')),
            ],
        ),
    ]