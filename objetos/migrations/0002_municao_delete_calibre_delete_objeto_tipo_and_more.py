# Generated by Django 4.0.4 on 2022-05-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calibre_municao', models.CharField(choices=[('38', 'calibre .38'), ('380', 'calibre .380'), ('40', 'calibre .40'), ('45', 'calibre .45')], max_length=3)),
                ('marca_municao', models.CharField(max_length=64)),
                ('modelo_municao', models.CharField(max_length=64)),
                ('valor_estimado_municao', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='calibre',
        ),
        migrations.DeleteModel(
            name='objeto_tipo',
        ),
        migrations.AddField(
            model_name='arma',
            name='calibre_arma',
            field=models.CharField(choices=[('38', 'calibre .38'), ('380', 'calibre .380'), ('40', 'calibre .40'), ('45', 'calibre .45'), ('N', 'não especificado')], default='N', max_length=3),
        ),
    ]
