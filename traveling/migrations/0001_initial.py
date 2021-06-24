# Generated by Django 3.2.4 on 2021-06-24 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('gugun', models.CharField(max_length=10)),
                ('latitude', models.CharField(max_length=60)),
                ('longitude', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=100)),
                ('call_number', models.CharField(max_length=30)),
                ('url', models.TextField()),
                ('image', models.TextField()),
                ('detail', models.TextField()),
                ('time', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='gugun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('call_number', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('foreign', models.CharField(max_length=50)),
                ('introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('inst_date', models.DateField(auto_now=True)),
                ('updt_date', models.DateField(auto_now=True)),
                ('mainkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveling.content')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('traffic', models.TextField()),
                ('break_time', models.CharField(max_length=20)),
                ('amenity', models.CharField(max_length=50)),
                ('mainkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveling.content')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('represent', models.CharField(max_length=200)),
                ('mainkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveling.content')),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('traffic', models.TextField()),
                ('cost', models.CharField(max_length=30)),
                ('amenity', models.CharField(max_length=50)),
                ('mainkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveling.content')),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('traffic', models.TextField()),
                ('break_time', models.CharField(max_length=20)),
                ('cost', models.CharField(max_length=30)),
                ('amenity', models.CharField(max_length=50)),
                ('mainkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveling.content')),
            ],
        ),
    ]
