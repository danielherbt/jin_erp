# Generated by Django 4.0.1 on 2022-08-11 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
                ('juridic', models.BooleanField(default=False, help_text='Si es persona jurídica', verbose_name='Jurídica')),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
            },
        ),
        migrations.CreateModel(
            name='HistoricalGenre',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('juridic', models.BooleanField(default=False, help_text='Si es persona jurídica', verbose_name='Jurídica')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Género',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
