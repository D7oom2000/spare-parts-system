# Generated by Django 4.0 on 2023-02-08 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_user_groups_alter_user_user_permissions'),
        ('SCP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_image',
            name='image_field',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='images/part/20230208-231457', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='workshop_image',
            name='image_field',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/profile/20230208-231457', width_field='imagewidth'),
        ),
        migrations.CreateModel(
            name='DabrhaRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_no', models.CharField(max_length=20, null=True)),
                ('P_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('car_manu', models.CharField(max_length=150)),
                ('car_name', models.CharField(max_length=150)),
                ('manufacture_year', models.CharField(max_length=10)),
                ('original', models.BooleanField()),
                ('desc', models.TextField()),
                ('offer_price', models.FloatField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='User.customer')),
            ],
        ),
        migrations.CreateModel(
            name='DabrhaOrders',
            fields=[
                ('order_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('price', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='User.customer')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store', to='User.store')),
            ],
        ),
    ]
