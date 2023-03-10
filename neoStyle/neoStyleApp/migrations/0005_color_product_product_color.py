# Generated by Django 4.1.6 on 2023-02-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoStyleApp', '0004_product_product_image2_product_product_image3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=models.ManyToManyField(to='neoStyleApp.color'),
        ),
    ]