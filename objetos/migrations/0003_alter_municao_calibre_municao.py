# Generated by Django 4.0.4 on 2022-05-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0002_municao_delete_calibre_delete_objeto_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municao',
            name='calibre_municao',
            field=models.CharField(choices=[('38', 'calibre .38'), ('380', 'calibre .380'), ('40', 'calibre .40'), ('45', 'calibre .45'), ('N', 'não especificado')], default='N', max_length=3),
        ),
    ]
