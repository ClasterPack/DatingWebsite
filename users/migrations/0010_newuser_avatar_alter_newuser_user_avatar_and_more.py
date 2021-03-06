# Generated by Django 4.0.1 on 2022-01-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_newuser_user_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='avatar',
            field=models.ImageField(default='avatars/default.png', upload_to='proficepic', verbose_name='аватар пользователя с водяным знаком'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='user_avatar',
            field=models.ImageField(default='avatars/default.png', upload_to='', verbose_name='аватар пользователя'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='user_sex',
            field=models.CharField(choices=[('-', 'Не выбран'), ('w', 'Женский'), ('m', 'Мужской')], max_length=1),
        ),
    ]
