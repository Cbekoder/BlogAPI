# Generated by Django 5.0 on 2023-12-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0002_muallif_email_maqola'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muallif',
            name='ism',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='muallif',
            name='yosh',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
