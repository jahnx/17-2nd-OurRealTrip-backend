# Generated by Django 3.1.7 on 2021-03-04 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('accommodation', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='accommodation_order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.accommodationorder'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user'),
        ),
        migrations.AddField(
            model_name='accommodationkeyword',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.accommodation'),
        ),
        migrations.AddField(
            model_name='accommodationkeyword',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.category'),
        ),
        migrations.AddField(
            model_name='accommodationimage',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.accommodation'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accommodation.address'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accommodation.city'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accommodation.host'),
        ),
    ]