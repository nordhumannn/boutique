# Generated by Django 4.1 on 2022-10-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_ordercheckout_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercheckout',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
