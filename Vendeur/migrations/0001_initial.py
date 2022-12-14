# Generated by Django 4.1 on 2022-08-06 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_secret', models.CharField(blank=True, default='', max_length=10000)),
                ('name', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=3, max_digits=6)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, max_length=255)),
                ('update_colis', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationColis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Addresse', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VendeurUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Masculine'), ('F', 'F??minine')], max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('adresse2', models.CharField(blank=True, max_length=255)),
                ('adresse3', models.CharField(blank=True, max_length=255)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('colis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paiement_colis', to='Vendeur.colis')),
                ('destination_colis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paiement_destination_colis', to='Vendeur.destinationcolis')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paiement_vendeur', to='Vendeur.vendeuruserprofile')),
            ],
        ),
        migrations.AddField(
            model_name='colis',
            name='destination_colis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colois_location_colis', to='Vendeur.destinationcolis'),
        ),
        migrations.AddField(
            model_name='colis',
            name='vendeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colois_vendeur', to='Vendeur.vendeuruserprofile'),
        ),
    ]
