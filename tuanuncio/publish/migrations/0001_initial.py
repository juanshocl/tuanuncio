# Generated by Django 3.0.6 on 2020-06-01 18:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advertisement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=50)),
                ('show_phones', models.BooleanField(default=False)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('url_website', models.URLField(default=None)),
                ('address', models.CharField(default=None, max_length=200)),
                ('latitude_longitude', models.CharField(default=None, max_length=200)),
                ('show_adress', models.BooleanField(default=False)),
                ('description', models.CharField(default=None, max_length=200)),
                ('image', models.ImageField(default=None, upload_to='static/img')),
                ('logo', models.ImageField(default=None, upload_to='static/img/logo')),
                ('incorporation_date', models.DateField(auto_now=True)),
                ('state', models.BooleanField(default=True)),
                ('includes_maps', models.BooleanField(default=False)),
                ('price_from', models.IntegerField(default=0)),
                ('price_to', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='credits',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('time_recharge', models.TimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='NameSocialNetworks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('NameDescriptions', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='phones',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('typePhone', models.CharField(max_length=50)),
                ('Number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_date', models.DateField()),
                ('closed', models.BooleanField(default=True)),
                ('from_hour', models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)], null=True)),
                ('to_hour', models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subscription_plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('valid_from', models.DateField(auto_now=True)),
                ('valid_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='typeA',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='social_networks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_socialNetwork', models.CharField(max_length=50)),
                ('red', models.ManyToManyField(default=None, to='publish.NameSocialNetworks')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday_from', models.PositiveSmallIntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (7, 'Domingo')], unique=True)),
                ('weekday_to', models.PositiveSmallIntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (7, 'Domingo')])),
                ('from_hour', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)])),
                ('to_hour', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)])),
                ('store', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='publish.advertisement')),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='Social_network',
            field=models.ManyToManyField(default=None, to='publish.social_networks'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='Type_advertisement',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='publish.typeA'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='credits_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='publish.credits'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='phones',
            field=models.ManyToManyField(default=None, to='publish.phones'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='subscription_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='publish.subscription_plan'),
        ),
    ]
