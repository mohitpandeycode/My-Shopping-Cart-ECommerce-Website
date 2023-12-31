# Generated by Django 4.2.5 on 2023-10-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(default='', max_length=5000)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('address', models.CharField(default='', max_length=300)),
                ('city', models.CharField(default='', max_length=200)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip_code', models.CharField(default='', max_length=20)),
                ('phone', models.CharField(default=0, max_length=12)),
            ],
        ),
    ]
