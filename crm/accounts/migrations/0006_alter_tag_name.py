# Generated by Django 4.1.1 on 2022-09-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Summer', 'Summer'), ('Kitchen', 'Kitchen')], max_length=200, null=True),
        ),
    ]