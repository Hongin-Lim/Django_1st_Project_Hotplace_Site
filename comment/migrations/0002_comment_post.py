# Generated by Django 4.0.1 on 2022-01-20 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hplace', '0005_board_menu_1_board_menu_2_board_menu_3_board_menu_4_and_more'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hplace.board'),
            preserve_default=False,
        ),
    ]
