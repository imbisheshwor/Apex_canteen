# Generated by Django 4.0.4 on 2022-07-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_photo', models.ImageField(upload_to='productPhotos/')),
                ('product_desc', models.TextField(max_length=500, null=True)),
                ('product_price', models.IntegerField()),
                ('product_active', models.BooleanField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
