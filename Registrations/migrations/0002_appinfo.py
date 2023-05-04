# Generated by Django 4.2 on 2023-04-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appName', models.CharField(default='unverified', max_length=64)),
                ('appProvider', models.CharField(default='unverified', max_length=64)),
                ('appCategory', models.CharField(default='unverified', max_length=64)),
                ('appDId', models.CharField(default='unverified', max_length=64)),
                ('appInstanceId', models.CharField(default='unverified', max_length=64)),
                ('endpoint', models.CharField(default='unverified', max_length=64)),
                ('appServiceRequired', models.CharField(default='unverified', max_length=64)),
                ('appServiceOptional', models.CharField(default='unverified', max_length=64)),
                ('appFeatureRequired', models.CharField(default='unverified', max_length=64)),
                ('appFeatureOptional', models.CharField(default='unverified', max_length=64)),
                ('isInsByMec', models.CharField(default='unverified', max_length=64)),
                ('appProfile', models.CharField(default='unverified', max_length=64)),
            ],
        ),
    ]