# Generated by Django 4.0.2 on 2022-02-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('video_link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'verbose_name': 'Home Banner',
                'verbose_name_plural': 'Home Banners',
            },
        ),
        migrations.CreateModel(
            name='LiveSaleSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('heading', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'LiveSaleSection',
                'verbose_name_plural': 'LiveSaleSections',
            },
        ),
        migrations.CreateModel(
            name='ShoppingX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
            ],
            options={
                'verbose_name': 'ShoppingX',
                'verbose_name_plural': 'ShoppingXs',
            },
        ),
        migrations.CreateModel(
            name='TrendingDeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
            ],
            options={
                'verbose_name': 'TrendingDeals',
                'verbose_name_plural': 'TrendingDeals',
            },
        ),
    ]