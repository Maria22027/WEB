# Generated by Django 5.1.2 on 2024-11-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_autor_login_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='imagens/')),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
