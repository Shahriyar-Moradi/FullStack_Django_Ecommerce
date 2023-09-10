# Generated by Django 4.0.4 on 2023-09-01 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_photo_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.DeleteModel(
            name='OderItem',
        ),
    ]
