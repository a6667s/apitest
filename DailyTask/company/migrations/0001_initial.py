# Generated by Django 3.2.7 on 2021-09-03 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('start_data', models.DateField()),
                ('education', models.CharField(blank=True, max_length=50, null=True)),
                ('experience', models.CharField(blank=True, max_length=50, null=True)),
                ('external_title', models.CharField(blank=True, max_length=50, null=True)),
                ('job_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.category')),
            ],
        ),
    ]
