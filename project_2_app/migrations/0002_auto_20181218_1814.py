# Generated by Django 2.0.5 on 2018-12-18 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_2_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='email_address', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
