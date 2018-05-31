# Generated by Django 2.0.5 on 2018-05-31 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0002_auto_20180530_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinformation',
            old_name='zip_Code',
            new_name='zip_code',
        ),
        migrations.AlterField(
            model_name='member',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chapter.Chapter'),
        ),
        migrations.AlterField(
            model_name='member',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chapter.MemberChurch'),
        ),
    ]
