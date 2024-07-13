# Generated by Django 5.0.6 on 2024-07-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_translate_email_ky_translate_email_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='translate',
            name='email_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Официальная почта'),
        ),
        migrations.AddField(
            model_name='translate',
            name='hotline_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Горячая линия'),
        ),
        migrations.AddField(
            model_name='translate',
            name='our_location_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='translate',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок баннера'),
        ),
    ]
