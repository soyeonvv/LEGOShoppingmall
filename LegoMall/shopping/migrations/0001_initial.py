# Generated by Django 3.2.9 on 2021-12-06 19:28

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
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('contact_numbers', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('hook_text', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField()),
                ('head_image', models.ImageField(blank=True, upload_to='lego/images/')),
                ('price', models.IntegerField()),
                ('age', models.IntegerField()),
                ('pcs', models.IntegerField()),
                ('Manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.manufacturer')),
            ],
        ),
    ]