# Generated by Django 4.2.3 on 2023-09-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', '男性'), ('F', '女性'), ('N', 'その他')], max_length=1)),
                ('addredss', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('allergy', models.ManyToManyField(related_name='allergy', to='ingredient.ingredient')),
                ('disliking_ingredients', models.ManyToManyField(related_name='disliking_ingredients', to='ingredient.ingredient')),
            ],
        ),
    ]
