# Generated by Django 4.0.1 on 2022-01-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_newuser_user_avatar_alter_newuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='user_avatar',
            field=models.ImageField(default='default.png', upload_to='avatars/', verbose_name='аватар пользователя'),
        ),
    ]
