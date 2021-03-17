# Generated by Django 3.1.5 on 2021-03-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cerendials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cerendial_name', models.CharField(max_length=50)),
                ('Cerendial_image', models.ImageField(default='', upload_to='assests/upload')),
            ],
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('client_image', models.ImageField(default='', upload_to='assests/upload')),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_designation', models.CharField(default='', max_length=50)),
                ('employee_desc', models.CharField(blank='True', max_length=1000)),
                ('employee_image', models.ImageField(default='', upload_to='assests/upload')),
            ],
        ),
        migrations.CreateModel(
            name='franchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_name', models.CharField(max_length=50)),
                ('franchise_image', models.ImageField(default='', upload_to='assests/upload')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg1_image', models.ImageField(default='', upload_to='assests/upload')),
                ('bg2_image', models.ImageField(default='', upload_to='assests/upload')),
                ('bg3_image', models.ImageField(default='', upload_to='assests/upload')),
                ('worker1_image', models.ImageField(default='', upload_to='assests/upload')),
                ('worker2_image', models.ImageField(default='', upload_to='assests/upload')),
                ('worker3_image', models.ImageField(default='', upload_to='assests/upload')),
            ],
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Machine_name', models.CharField(max_length=50)),
                ('Machine_image', models.ImageField(default='', upload_to='assests/upload')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(blank='True', max_length=1000)),
                ('image', models.ImageField(default='', upload_to='assests/upload')),
            ],
        ),
    ]
