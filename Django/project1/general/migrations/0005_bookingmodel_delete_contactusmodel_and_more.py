# Generated by Django 5.0.2 on 2024-02-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_contactusmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=2)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=25)),
                ('roomtype', models.CharField(max_length=10)),
                ('paymentmethod', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactusModel',
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='contact',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
