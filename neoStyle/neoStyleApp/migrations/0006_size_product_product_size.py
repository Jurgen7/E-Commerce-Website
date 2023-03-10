# Generated by Django 4.1.6 on 2023-02-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoStyleApp', '0005_color_product_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('size_id', models.AutoField(primary_key=True, serialize=False)),
                ('size_category', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.ManyToManyField(to='neoStyleApp.size'),
        ),
    ]