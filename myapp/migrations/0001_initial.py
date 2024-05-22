# Generated by Django 3.2.25 on 2024-05-22 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('emeail', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('Maharashtra', 'Maharashtra'), ('Kerala', 'Kerala'), ('Bihar', 'Bihar')], max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pimage', models.ImageField(blank=True, upload_to='myimage')),
                ('pfile', models.FileField(blank=True, upload_to='myfile')),
            ],
        ),
    ]
