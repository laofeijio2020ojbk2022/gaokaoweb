# Generated by Django 3.2.20 on 2023-08-12 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScMinAna',
            fields=[
                ('min_sc_id', models.AutoField(primary_key=True, serialize=False)),
                ('min_st_school_name', models.CharField(blank=True, db_column='min_ST_School_name', max_length=1024, null=True)),
                ('min_pro_name', models.CharField(blank=True, db_column='min_Pro_name', max_length=1024, null=True)),
                ('min_st_name', models.IntegerField(blank=True, db_column='min_ST_name', null=True)),
                ('min_st_local_batch_name', models.CharField(blank=True, db_column='min_ST_Local_batch_name', max_length=1024, null=True)),
                ('min_st_min_section', models.IntegerField(blank=True, db_column='min_ST_Min_section', null=True)),
            ],
            options={
                'db_table': 'sc_min_ana',
            },
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='pro',
            field=models.ForeignKey(db_column='Pro_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app01.proindex', verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_average',
            field=models.IntegerField(blank=True, db_column='ST_Average', null=True, verbose_name='平均分'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_level1_name',
            field=models.CharField(blank=True, db_column='ST_Level1_name', max_length=256, null=True, verbose_name='类别1'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_level2_name',
            field=models.CharField(blank=True, db_column='ST_Level2_name', max_length=256, null=True, verbose_name='类别2'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_level3_name',
            field=models.CharField(blank=True, db_column='ST_Level3_name', max_length=256, null=True, verbose_name='类别3'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_local_batch_name',
            field=models.CharField(blank=True, db_column='ST_Local_batch_name', max_length=256, null=True, verbose_name='批次'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_max',
            field=models.IntegerField(blank=True, db_column='ST_Max', null=True, verbose_name='最高分'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_min',
            field=models.IntegerField(blank=True, db_column='ST_Min', null=True, verbose_name='最低分'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_min_section',
            field=models.IntegerField(blank=True, db_column='ST_Min_section', null=True, verbose_name='最低位次'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_school_name',
            field=models.CharField(db_column='ST_School_name', max_length=256, verbose_name='学校名称'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_sg_info',
            field=models.CharField(blank=True, db_column='ST_Sg_info', max_length=1024, null=True, verbose_name='选课要求'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_spname',
            field=models.CharField(blank=True, db_column='ST_Spname', max_length=1024, null=True, verbose_name='专业'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_type',
            field=models.CharField(blank=True, db_column='ST_Type', max_length=256, null=True, verbose_name='分科'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_year',
            field=models.IntegerField(blank=True, db_column='ST_Year', null=True, verbose_name='年份'),
        ),
        migrations.AlterField(
            model_name='scoretable',
            name='st_zslx_name',
            field=models.CharField(blank=True, db_column='ST_Zslx_name', max_length=256, null=True, verbose_name='类别'),
        ),
    ]
