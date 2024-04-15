/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2024/4/15 22:23:50                           */
/*==============================================================*/


drop table if exists Notice;

drop table if exists People;

drop table if exists Pro_Index;

drop table if exists School_Index;

drop table if exists School_Info;

drop table if exists School_Logal;

drop table if exists Score_Table;

/*==============================================================*/
/* Table: Notice                                                */
/*==============================================================*/
create table Notice
(
   N_id                 int not null auto_increment,
   P_id                 int not null,
   N_name               varchar(256),
   N_info               varchar(1024),
   primary key (N_id)
);

/*==============================================================*/
/* Table: People                                                */
/*==============================================================*/
create table People
(
   P_id                 int not null auto_increment,
   P_name               varchar(256) not null,
   P_password           varchar(256) not null,
   P_sex                int,
   P_age                int,
   P_birth              date,
   P_word               varchar(1024),
   P_picture            longblob,
   P_score              int,
   P_pro                varchar(256),
   P_sp                 varchar(256),
   P_adm                int,
   primary key (P_id)
);

/*==============================================================*/
/* Table: Pro_Index                                             */
/*==============================================================*/
create table Pro_Index
(
   Pro_id               int not null,
   Pro_name             varchar(256) not null,
   primary key (Pro_id)
);

/*==============================================================*/
/* Table: School_Index                                          */
/*==============================================================*/
create table School_Index
(
   SI_id                int not null,
   SI_name              varchar(256) not null,
   Img_1                varchar(1024),
   Img_2                varchar(1024),
   Img_3                varchar(1024),
   Img_4                varchar(1024),
   Img_5                varchar(1024),
   Img_6                varchar(1024),
   Img_name             varchar(1024),
   primary key (SI_id)
);

/*==============================================================*/
/* Table: School_Info                                           */
/*==============================================================*/
create table School_Info
(
   SC_id                int not null,
   SC_name              varchar(256) not null,
   SC_code_enroll       varchar(256),
   SC_belong            varchar(256),
   SC_f985              int,
   SC_f211              int,
   SC_num_subject       int,
   SC_num_master        int,
   SC_num_doctor        int,
   SC_num_academician   int,
   SC_num_library       varchar(256),
   SC_num_lab           int,
   SC_province_id       int,
   SC_is_recruitment    int,
   SC_create_date       int,
   SC_area              int,
   SC_old_name          varchar(256),
   SC_is_fenxiao        int,
   SC_short             varchar(256),
   SC_ruanke_rank       int,
   SC_wsl_rank          int,
   SC_qs_rank           int,
   SC_xyh_rank          int,
   SC_eol_rank          int,
   SC_us_rank           int,
   SC_is_logo           int,
   SC_bdold_name        varchar(256),
   SC_gbh_num           int,
   SC_level_name        varchar(256),
   SC_type_name         varchar(256),
   SC_school_nature_name varchar(256),
   SC_dual_class_name   varchar(256),
   SC_xueke_rank        varchar(256),
   SC_province_name     varchar(256),
   SC_city_name         varchar(256),
   SC_town_name         varchar(256),
   SC_weiwangzhan       varchar(256),
   SC_yjszs             varchar(256),
   SC_xiaoyuan          varchar(256),
   SC_email             varchar(256),
   SC_school_email      varchar(256),
   SC_address           varchar(256),
   SC_postcode          varchar(256),
   SC_site              varchar(256),
   SC_school_site       varchar(256),
   SC_phone             varchar(256),
   SC_content           varchar(1024),
   SC_dualclass         varchar(1024),
   SC_special           varchar(1024),
   SC_nature_name       varchar(256),
   SC_province_score_year int,
   SC_qs_world          varchar(256),
   SC_fenxiao           varchar(1024),
   SC_gbh_url           varchar(1024),
   SC_jobrate           varchar(1024),
   SC_job_province      varchar(1024),
   SC_attr              varchar(1024),
   SC_company           varchar(4096),
   SC_vote              varchar(1024),
   primary key (SC_id)
);

/*==============================================================*/
/* Table: School_Logal                                          */
/*==============================================================*/
create table School_Logal
(
   Logao_id             int not null,
   Logal_name           varchar(256),
   Logal_data           longblob,
   primary key (Logao_id)
);

/*==============================================================*/
/* Table: Score_Table                                           */
/*==============================================================*/
create table Score_Table
(
   ST_id                bigint not null auto_increment,
   Pro_id               int not null,
   SI_id                int not null,
   ST_School_name       varchar(256) not null,
   ST_Year              int,
   ST_Type              varchar(256),
   ST_Spname            varchar(1024),
   ST_Max               int,
   ST_Min               int,
   ST_Average           int,
   ST_Min_section       int,
   ST_Info              varchar(1024),
   ST_Level1_name       varchar(256),
   ST_Level2_name       varchar(256),
   ST_Level3_name       varchar(256),
   ST_Zslx_name         varchar(256),
   ST_Local_batch_name  varchar(256),
   ST_Sg_info           varchar(1024),
   ST_Sg_xuanke         varchar(1024),
   primary key (ST_id)
);

alter table Notice add constraint FK_P_N foreign key (P_id)
      references People (P_id) on delete restrict on update restrict;

alter table Score_Table add constraint FK_Pro_ST foreign key (Pro_id)
      references Pro_Index (Pro_id) on delete restrict on update restrict;

alter table Score_Table add constraint FK_SI_ST foreign key (SI_id)
      references School_Index (SI_id) on delete restrict on update restrict;

