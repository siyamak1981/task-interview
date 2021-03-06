# Generated by Django 4.0.5 on 2022-07-02 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_alter_rate_product_alter_rate_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='products.product'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate', to=settings.AUTH_USER_MODEL),
        ),
    ]
