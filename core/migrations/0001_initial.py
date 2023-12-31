# Generated by Django 4.2.5 on 2023-11-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('resumo', models.TextField()),
                ('experiencia', models.TextField()),
                ('formacao', models.TextField()),
                ('habilidades', models.TextField()),
                ('ano', models.IntegerField()),
                ('instituicao', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('periodo', models.CharField(max_length=20)),
                ('foto', models.ImageField(default='ok', upload_to='media/')),
            ],
        ),
    ]
