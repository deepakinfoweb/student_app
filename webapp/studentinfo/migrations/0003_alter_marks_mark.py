# Generated by Django 3.2 on 2021-04-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0002_auto_20210412_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='mark',
            field=models.DecimalField(decimal_places=2, max_digits=30),
        ),
    ]
