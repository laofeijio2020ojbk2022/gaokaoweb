# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RatePredict(models.Model):
    rate_id = models.AutoField(primary_key=True)
    ra_school_id = models.IntegerField(db_column='ra_School_id', blank=True, null=True)  # Field name made lowercase.
    ra_school_name = models.CharField(db_column='ra_School_name', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ra_loc_province = models.CharField(db_column='ra_Loc_province', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ra_pro_id = models.IntegerField(db_column='ra_Pro_id', blank=True, null=True)  # Field name made lowercase.
    ra_pro_name = models.CharField(db_column='ra_Pro_name', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ra_avg_min_2021 = models.IntegerField(db_column='ra_Avg_Min_2021', blank=True, null=True)  # Field name made lowercase.
    ra_avg_min_2022 = models.IntegerField(db_column='ra_Avg_Min_2022', blank=True, null=True)  # Field name made lowercase.
    ra_score_rate = models.FloatField(db_column='ra_Score_rate', blank=True, null=True)  # Field name made lowercase.
    ra_avg_min_section_2021 = models.IntegerField(db_column='ra_Avg_Min_section_2021', blank=True, null=True)  # Field name made lowercase.
    ra_avg_min_section_2022 = models.IntegerField(db_column='ra_Avg_Min_section_2022', blank=True, null=True)  # Field name made lowercase.
    ra_section_rate = models.FloatField(blank=True, null=True)
    ra_average_score = models.FloatField(blank=True, null=True)
    ra_average_section = models.FloatField(blank=True, null=True)
    ra_predict_score = models.IntegerField(blank=True, null=True)
    ra_predict_section = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'rate_predict'


class NumSpname(models.Model):
    si_id = models.AutoField(primary_key=True)
    si_st_school_name = models.CharField(db_column='si_ST_School_name', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    si_pro_name = models.CharField(db_column='si_Pro_name', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    si_st_year = models.IntegerField(db_column='si_ST_Year', blank=True, null=True)  # Field name made lowercase.
    si_st_spname = models.IntegerField(db_column='si_ST_Spname', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'num_spname'


class ScMinAna(models.Model):
    min_sc_id = models.AutoField(primary_key=True)
    min_st_school_name = models.CharField(db_column='min_ST_School_name', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    min_pro_name = models.CharField(db_column='min_Pro_name', max_length=1024, blank=True, null=True, verbose_name="省份")  # Field name made lowercase.
    min_st_name = models.IntegerField(db_column='min_ST_name', blank=True, null=True, verbose_name="年份")  # Field name made lowercase.
    min_st_local_batch_name = models.CharField(db_column='min_ST_Local_batch_name', max_length=1024, blank=True, null=True, verbose_name="批次")  # Field name made lowercase.
    min_st_min_section = models.IntegerField(db_column='min_ST_Min_section', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'sc_min_ana'


class People(models.Model):
    p_id = models.AutoField(db_column='P_id', primary_key=True)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_name', max_length=256)  # Field name made lowercase.
    p_password = models.CharField(db_column='P_password', max_length=256)  # Field name made lowercase.
    p_sex = models.IntegerField(db_column='P_sex', blank=True, null=True)  # Field name made lowercase.
    p_age = models.IntegerField(db_column='P_age', blank=True, null=True)  # Field name made lowercase.
    p_birth = models.DateField(db_column='P_birth', blank=True, null=True)  # Field name made lowercase.
    p_word = models.CharField(db_column='P_word', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    p_picture = models.TextField(db_column='P_picture', blank=True, null=True)  # Field name made lowercase.
    p_score = models.IntegerField(db_column='P_score', blank=True, null=True)  # Field name made lowercase.
    p_pro = models.CharField(db_column='P_pro', max_length=256, blank=True, null=True)  # Field name made lowercase.
    p_sp = models.CharField(db_column='P_sp', max_length=256, blank=True, null=True)  # Field name made lowercase.
    p_adm = models.IntegerField(db_column='P_adm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'People'


class Notice(models.Model):
    n_id = models.AutoField(db_column='N_id', primary_key=True)  # Field name made lowercase.
    p = models.ForeignKey('People', models.DO_NOTHING, db_column='P_id')  # Field name made lowercase.
    n_name = models.CharField(db_column='N_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    n_info = models.CharField(db_column='N_info', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'Notice'


class ProIndex(models.Model):
    pro_id = models.IntegerField(db_column='Pro_id', primary_key=True)  # Field name made lowercase.
    pro_name = models.CharField(db_column='Pro_name', max_length=256)  # Field name made lowercase.

    def __str__(self):
        return self.pro_name

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'Pro_Index'


class SchoolIndex(models.Model):
    si_id = models.IntegerField(db_column='SI_id', primary_key=True)  # Field name made lowercase.
    si_name = models.CharField(db_column='SI_name', max_length=256)  # Field name made lowercase.
    img_1 = models.CharField(db_column='Img_1', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    img_2 = models.CharField(db_column='Img_2', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    img_3 = models.CharField(db_column='Img_3', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    img_4 = models.CharField(db_column='Img_4', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    img_5 = models.CharField(db_column='Img_5', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    img_6 = models.CharField(db_column='Img_6', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    img_name = models.CharField(db_column='Img_name', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'School_Index'


class SchoolInfo(models.Model):
    sc_id = models.IntegerField(db_column='SC_id', primary_key=True)  # Field name made lowercase.
    sc_name = models.CharField(db_column='SC_name', max_length=256)  # Field name made lowercase.
    sc_code_enroll = models.CharField(db_column='SC_code_enroll', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_belong = models.CharField(db_column='SC_belong', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_f985 = models.IntegerField(db_column='SC_f985', blank=True, null=True)  # Field name made lowercase.
    sc_f211 = models.IntegerField(db_column='SC_f211', blank=True, null=True)  # Field name made lowercase.
    sc_num_subject = models.IntegerField(db_column='SC_num_subject', blank=True, null=True)  # Field name made lowercase.
    sc_num_master = models.IntegerField(db_column='SC_num_master', blank=True, null=True)  # Field name made lowercase.
    sc_num_doctor = models.IntegerField(db_column='SC_num_doctor', blank=True, null=True)  # Field name made lowercase.
    sc_num_academician = models.IntegerField(db_column='SC_num_academician', blank=True, null=True)  # Field name made lowercase.
    sc_num_library = models.CharField(db_column='SC_num_library', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_num_lab = models.IntegerField(db_column='SC_num_lab', blank=True, null=True)  # Field name made lowercase.
    sc_province_id = models.IntegerField(db_column='SC_province_id', blank=True, null=True)  # Field name made lowercase.
    sc_is_recruitment = models.IntegerField(db_column='SC_is_recruitment', blank=True, null=True)  # Field name made lowercase.
    sc_create_date = models.IntegerField(db_column='SC_create_date', blank=True, null=True)  # Field name made lowercase.
    sc_area = models.IntegerField(db_column='SC_area', blank=True, null=True)  # Field name made lowercase.
    sc_old_name = models.CharField(db_column='SC_old_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_is_fenxiao = models.IntegerField(db_column='SC_is_fenxiao', blank=True, null=True)  # Field name made lowercase.
    sc_short = models.CharField(db_column='SC_short', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_ruanke_rank = models.IntegerField(db_column='SC_ruanke_rank', blank=True, null=True)  # Field name made lowercase.
    sc_wsl_rank = models.IntegerField(db_column='SC_wsl_rank', blank=True, null=True)  # Field name made lowercase.
    sc_qs_rank = models.IntegerField(db_column='SC_qs_rank', blank=True, null=True)  # Field name made lowercase.
    sc_xyh_rank = models.IntegerField(db_column='SC_xyh_rank', blank=True, null=True)  # Field name made lowercase.
    sc_eol_rank = models.IntegerField(db_column='SC_eol_rank', blank=True, null=True)  # Field name made lowercase.
    sc_us_rank = models.IntegerField(db_column='SC_us_rank', blank=True, null=True)  # Field name made lowercase.
    sc_is_logo = models.IntegerField(db_column='SC_is_logo', blank=True, null=True)  # Field name made lowercase.
    sc_bdold_name = models.CharField(db_column='SC_bdold_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_gbh_num = models.IntegerField(db_column='SC_gbh_num', blank=True, null=True)  # Field name made lowercase.
    sc_level_name = models.CharField(db_column='SC_level_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_type_name = models.CharField(db_column='SC_type_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_school_nature_name = models.CharField(db_column='SC_school_nature_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_dual_class_name = models.CharField(db_column='SC_dual_class_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_xueke_rank = models.CharField(db_column='SC_xueke_rank', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_province_name = models.CharField(db_column='SC_province_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_city_name = models.CharField(db_column='SC_city_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_town_name = models.CharField(db_column='SC_town_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_weiwangzhan = models.CharField(db_column='SC_weiwangzhan', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_yjszs = models.CharField(db_column='SC_yjszs', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_xiaoyuan = models.CharField(db_column='SC_xiaoyuan', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_email = models.CharField(db_column='SC_email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_school_email = models.CharField(db_column='SC_school_email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_address = models.CharField(db_column='SC_address', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_postcode = models.CharField(db_column='SC_postcode', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_site = models.CharField(db_column='SC_site', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_school_site = models.CharField(db_column='SC_school_site', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_phone = models.CharField(db_column='SC_phone', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_content = models.CharField(db_column='SC_content', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sc_dualclass = models.CharField(db_column='SC_dualclass', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sc_special = models.CharField(db_column='SC_special', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sc_nature_name = models.CharField(db_column='SC_nature_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_province_score_year = models.IntegerField(db_column='SC_province_score_year', blank=True, null=True)  # Field name made lowercase.
    sc_qs_world = models.CharField(db_column='SC_qs_world', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sc_fenxiao = models.CharField(db_column='SC_fenxiao', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sc_gbh_url = models.CharField(db_column='SC_gbh_url', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sc_jobrate = models.CharField(db_column='SC_jobrate', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sc_job_province = models.CharField(db_column='SC_job_province', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sc_attr = models.CharField(db_column='SC_attr', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sc_company = models.CharField(db_column='SC_company', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    sc_vote = models.CharField(db_column='SC_vote', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'School_Info'


class SchoolLogal(models.Model):
    logao_id = models.IntegerField(db_column='Logao_id', primary_key=True)  # Field name made lowercase.
    logal_name = models.CharField(db_column='Logal_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    logal_data = models.TextField(db_column='Logal_data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'School_Logal'


class ScoreTable(models.Model):
    st_id = models.BigAutoField(db_column='ST_id', primary_key=True)  # Field name made lowercase.
    pro = models.ForeignKey(ProIndex, models.DO_NOTHING, db_column='Pro_id', verbose_name="省份")  # Field name made lowercase.
    si = models.ForeignKey(SchoolIndex, models.DO_NOTHING, db_column='SI_id')  # Field name made lowercase.
    st_school_name = models.CharField(db_column='ST_School_name', max_length=256, verbose_name="学校名称")  # Field name made lowercase.
    st_year = models.IntegerField(db_column='ST_Year', blank=True, null=True, verbose_name="年份")  # Field name made lowercase.
    st_type = models.CharField(db_column='ST_Type', max_length=256, blank=True, null=True, verbose_name="分科")  # Field name made lowercase.
    st_spname = models.CharField(db_column='ST_Spname', max_length=1024, blank=True, null=True, verbose_name="专业")  # Field name made lowercase.
    st_max = models.IntegerField(db_column='ST_Max', blank=True, null=True, verbose_name="最高分")  # Field name made lowercase.
    st_min = models.IntegerField(db_column='ST_Min', blank=True, null=True, verbose_name="最低分")  # Field name made lowercase.
    st_average = models.IntegerField(db_column='ST_Average', blank=True, null=True, verbose_name="平均分")  # Field name made lowercase.
    st_min_section = models.IntegerField(db_column='ST_Min_section', blank=True, null=True, verbose_name="最低位次")  # Field name made lowercase.
    st_info = models.CharField(db_column='ST_Info', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    st_level1_name = models.CharField(db_column='ST_Level1_name', max_length=256, blank=True, null=True, verbose_name="类别1")  # Field name made lowercase.
    st_level2_name = models.CharField(db_column='ST_Level2_name', max_length=256, blank=True, null=True, verbose_name="类别2")  # Field name made lowercase.
    st_level3_name = models.CharField(db_column='ST_Level3_name', max_length=256, blank=True, null=True, verbose_name="类别3")  # Field name made lowercase.
    st_zslx_name = models.CharField(db_column='ST_Zslx_name', max_length=256, blank=True, null=True, verbose_name="类别")  # Field name made lowercase.
    st_local_batch_name = models.CharField(db_column='ST_Local_batch_name', max_length=256, blank=True, null=True, verbose_name="批次")  # Field name made lowercase.
    st_sg_info = models.CharField(db_column='ST_Sg_info', max_length=1024, blank=True, null=True, verbose_name="选课要求")  # Field name made lowercase.
    st_sg_xuanke = models.CharField(db_column='ST_Sg_xuanke', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'Score_Table'


class App01Userinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=10)

    class Meta:
        # managed = False
        app_label = 'app01'
        db_table = 'app01_userinfo'

