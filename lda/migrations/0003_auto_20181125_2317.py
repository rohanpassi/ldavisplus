# Generated by Django 2.1.3 on 2018-11-25 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lda', '0002_auto_20181125_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='sentiment_polarity',
            field=models.TextField(null=True),
        ),
    ]
