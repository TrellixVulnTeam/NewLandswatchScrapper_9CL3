# Generated by Django 2.2 on 2021-03-24 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountId', models.BigIntegerField()),
                ('acres', models.FloatField()),
                ('adTargetingCountyId', models.BigIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('baths', models.BigIntegerField()),
                ('beds', models.BigIntegerField()),
                ('brokerCompany', models.CharField(max_length=255)),
                ('brokerName', models.CharField(max_length=255)),
                ('Url', models.URLField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('cityID', models.BigIntegerField()),
                ('companyLogoDocumentId', models.BigIntegerField()),
                ('county', models.CharField(max_length=255)),
                ('countyId', models.BigIntegerField()),
                ('description', models.TextField(max_length=255)),
                ('hasHouse', models.BooleanField()),
                ('hasVideo', models.BooleanField()),
                ('hasVirtualTour', models.BigIntegerField()),
                ('imageCount', models.BigIntegerField()),
                ('imageAltTextDisplay', models.CharField(max_length=255)),
                ('isHeadlineAd', models.BooleanField()),
                ('lwPropertyId', models.BigIntegerField()),
                ('isALC', models.BigIntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('price', models.FloatField()),
                ('types', models.TextField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=20)),
                ('status1', models.CharField(max_length=255)),
                ('zip', models.BigIntegerField()),
                ('Rate', models.FloatField()),
                ('Descrpt', models.TextField(default='!', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusMaster',
            fields=[
                ('status', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('publish_date', models.DateTimeField()),
                ('views', models.IntegerField(default=0)),
                ('reviewed', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Author')),
                ('categories', models.ManyToManyField(to='core.Category')),
            ],
        ),
    ]
