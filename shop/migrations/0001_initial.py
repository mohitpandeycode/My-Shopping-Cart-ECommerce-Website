# Generated by Django 4.2.5 on 2023-09-26 07:03
# its genrated when after manage.py migrate we can run manage.py makemigrations
# after makemigrations if we run manage.py migrate  again then the database connect with product finally.
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
