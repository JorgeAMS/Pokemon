# Generated by Django 3.1.2 on 2020-10-03 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='evolutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evolution_secuence', models.IntegerField()),
                ('evolution', models.CharField(max_length=50)),
                ('poke_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokeinfo.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='basestats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=50)),
                ('poke_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokeinfo.pokemon')),
            ],
        ),
    ]