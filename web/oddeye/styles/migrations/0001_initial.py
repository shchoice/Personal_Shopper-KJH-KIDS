# Generated by Django 3.0.6 on 2020-06-10 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('like', models.IntegerField()),
                ('tag', models.CharField(max_length=30)),
                ('style', models.IntegerField()),
            ],
            options={
                'verbose_name': '스타',
                'verbose_name_plural': '스타',
                'db_table': 'star',
            },
        ),
        migrations.CreateModel(
            name='Star_embedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_embedding', models.CharField(max_length=1000)),
                ('no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='styles.Star')),
            ],
            options={
                'verbose_name': '스타 임베딩',
                'verbose_name_plural': '스타 임베딩 값',
                'db_table': 'star_embedding',
            },
        ),
    ]
