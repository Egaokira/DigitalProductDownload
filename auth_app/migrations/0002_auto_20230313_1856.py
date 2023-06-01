# Generated by Django 3.2.16 on 2023-03-13 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('useri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DigitalProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField()),
                ('product_title', models.TextField()),
                ('has_serial_keys', models.BooleanField(default=False)),
                ('has_file', models.BooleanField(default=False)),
                ('isall', models.BooleanField(default=True)),
                ('productSKU', models.TextField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField()),
                ('order_name', models.TextField()),
                ('quantity', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.digitalproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='digital_product_files/')),
                ('has_serial_keys', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.digitalproduct')),
            ],
        ),
        migrations.CreateModel(
            name='SerialKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('is_used', models.BooleanField(default=False)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.variant')),
            ],
        ),
        migrations.CreateModel(
            name='OrderKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.order')),
                ('serial_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.serialkey')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.variant'),
        ),
        migrations.CreateModel(
            name='DownloadLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True)),
                ('size', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.customer')),
                ('serial_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.serialkey')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.variant')),
            ],
        ),
    ]
