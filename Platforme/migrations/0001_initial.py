# Generated by Django 4.1 on 2022-08-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('site_adresse', models.CharField(max_length=255)),
                ('copyright', models.CharField(max_length=255)),
                ('site_email', models.CharField(max_length=255)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
    ]
