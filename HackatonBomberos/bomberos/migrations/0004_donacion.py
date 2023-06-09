# Generated by Django 4.2 on 2023-06-10 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bomberos', '0003_reportefalla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('cuartel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.cuartel')),
            ],
        ),
    ]
