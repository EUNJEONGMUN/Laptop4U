# Generated by Django 3.2.9 on 2021-12-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='final_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='first_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='review',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='sales_price',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
