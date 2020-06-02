# Generated by Django 3.0.6 on 2020-06-02 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='region',
            fields=[
                ('Codregion', models.CharField(default=None, max_length=2, primary_key=True, serialize=False)),
                ('RegionName', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='credits_id',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='image',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='includes_maps',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='latitude_longitude',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='phones',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='price_from',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='price_to',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='subscription_type',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='whatsapp',
            field=models.CharField(default=None, max_length=11),
        ),
        migrations.CreateModel(
            name='comuna',
            fields=[
                ('CodComuna', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('ComunaName', models.CharField(default=None, max_length=50)),
                ('Reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publish.region')),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='comuna',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='publish.comuna'),
        ),
    ]
