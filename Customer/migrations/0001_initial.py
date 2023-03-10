# Generated by Django 4.1.4 on 2022-12-29 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Order',
            fields=[
                ('co_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('C_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomerOders', to='User.customer')),
                ('S_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StoreOders', to='User.store')),
            ],
        ),
    ]
