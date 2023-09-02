# Generated by Django 4.1.7 on 2023-08-28 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('cateory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
