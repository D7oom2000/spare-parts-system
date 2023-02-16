# Generated by Django 4.0 on 2023-02-13 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_user_groups_alter_user_user_permissions'),
        ('SCP', '0005_alter_dabrharequest_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dabrharequest',
            name='has_an_offer',
        ),
        migrations.RemoveField(
            model_name='dabrharequest',
            name='offer_price',
        ),
        migrations.AlterField(
            model_name='store_image',
            name='image_field',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='images/part/20230213-195034', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='workshop_image',
            name='image_field',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/profile/20230213-195034', width_field='imagewidth'),
        ),
        migrations.CreateModel(
            name='dabrha_offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_price', models.FloatField()),
                ('dabrha_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='d_request', to='SCP.dabrharequest')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_made_offer', to='User.store')),
            ],
        ),
    ]
