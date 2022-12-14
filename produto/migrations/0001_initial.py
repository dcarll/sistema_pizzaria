# Generated by Django 4.1 on 2022-09-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('desc_curta', models.CharField(max_length=255)),
                ('desc_longa', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('preco_marketing', models.FloatField(verbose_name='Preço')),
                ('preco_marketing_promocional', models.FloatField(default=0, verbose_name='Preço promo')),
                ('tipo', models.CharField(choices=[('D', 'Doce'), ('S', 'Salgada')], default='V', max_length=1)),
                ('ingredientes', models.ManyToManyField(blank=True, to='produto.ingredientes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
