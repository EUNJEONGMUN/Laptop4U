# Generated by Django 3.2.9 on 2021-11-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_choice_choice_contents'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_contents',
            field=models.CharField(max_length=45, null=True),
        ),
    ]