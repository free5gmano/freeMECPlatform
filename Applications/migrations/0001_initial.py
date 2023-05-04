# Generated by Django 4.2 on 2023-04-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DnsRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appInstanceId', models.CharField(default='unverified', max_length=64)),
                ('dnsRuleId', models.CharField(default='unverified', max_length=64)),
                ('domainName', models.CharField(default='unverified', max_length=64)),
                ('ipAddressType', models.CharField(default='unverified', max_length=64)),
                ('ipAddress', models.CharField(default='unverified', max_length=64)),
                ('ttl', models.CharField(default='unverified', max_length=64)),
                ('state', models.CharField(default='unverified', max_length=64)),
            ],
        ),
    ]