# Generated by Django 4.1 on 2022-09-02 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('publicado', models.DateTimeField(auto_now=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'ingrediente',
                'verbose_name_plural': 'ingredientes',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('publicado', models.DateTimeField(auto_now=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao_pizza', models.TextField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ingredientes', models.ManyToManyField(blank=True, to='pizza.ingredientes')),
            ],
            options={
                'verbose_name': 'pizza',
                'verbose_name_plural': 'pizzas',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('publicado', models.DateTimeField(auto_now=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=255)),
                ('observacao', models.TextField(blank=True)),
                ('pizza', models.ManyToManyField(to='pizza.pizza')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('publicado', models.DateTimeField(auto_now=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=255)),
                ('texto', models.TextField()),
                ('pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizza.pizza')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('publicado', models.DateTimeField(auto_now=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('tituto', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('nota', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.pizza')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_pizza', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Avalia????o',
                'verbose_name_plural': 'Avalia????es',
            },
        ),
    ]
