# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse



class Food_Desert(models.Model):
    state = models.CharField(db_column='st', blank=True, null=True, max_length=3)
    county = models.TextField(db_column='County', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    pop2010 = models.FloatField(db_column='POP2010', blank=True, null=True)  # Field name made lowercase.
    num_fd = models.IntegerField(blank=True, null=True)
    pop_in_des = models.FloatField(blank=True, null=True)
    perc_lila = models.FloatField(blank=True, null=True)
    n_tracts = models.FloatField(blank=True, null=True)
    urban_des = models.FloatField(blank=True, null=True)
    rural_des = models.FloatField(blank=True, null=True)
    n_urban = models.FloatField(blank=True, null=True)
    n_rural = models.FloatField(blank=True, null=True)
    des_percent = models.FloatField(blank=True, null=True)
    lowincometracts = models.FloatField(db_column='LowIncomeTracts', blank=True, null=True)  # Field name made lowercase.
    low_vehicle_tracts = models.FloatField(blank=True, null=True)
    total_housing_units = models.FloatField(blank=True, null=True)
    pop_in_group_housing = models.FloatField(blank=True, null=True)
    pop_lila = models.FloatField(db_column='pop_LILA', blank=True, null=True)  # Field name made lowercase.
    state_pop_ratio = models.FloatField(blank=True, null=True)
    state_tract_ratio = models.FloatField(blank=True, null=True)
    cnty_obesity_pct_adj = models.FloatField(blank=True, null=True)
    cnty_dm_pct_adj = models.FloatField(blank=True, null=True)
    cnty_inactive_pct_adj = models.FloatField(blank=True, null=True)
    adolescent_births = models.FloatField(db_column='Adolescent_births', blank=True, null=True)  # Field name made lowercase.
    abr = models.FloatField(db_column='ABR', blank=True, null=True)  # Field name made lowercase.
    p_hs_edatt = models.FloatField(blank=True, null=True)
    pc_phys_r = models.FloatField(db_column='PC_PHYS_R', blank=True, null=True)  # Field name made lowercase.
    dentist_r = models.FloatField(db_column='DENTIST_R', blank=True, null=True)  # Field name made lowercase.
    psych_r = models.FloatField(db_column='PSYCH_R', blank=True, null=True)  # Field name made lowercase.
    pct_hspnc = models.FloatField(db_column='PCT_HSPNC', blank=True, null=True)  # Field name made lowercase.
    pct_white = models.FloatField(db_column='PCT_WHITE', blank=True, null=True)  # Field name made lowercase.
    pct_black = models.FloatField(db_column='PCT_BLACK', blank=True, null=True)  # Field name made lowercase.
    pct_asian = models.FloatField(db_column='PCT_ASIAN', blank=True, null=True)  # Field name made lowercase.
    pct_amind_esk = models.FloatField(db_column='PCT_AMIND_ESK', blank=True, null=True)  # Field name made lowercase.
    pct_islander = models.FloatField(db_column='PCT_ISLANDER', blank=True, null=True)  # Field name made lowercase.
    pct_multi = models.FloatField(db_column='PCT_MULTI', blank=True, null=True)  # Field name made lowercase.
    pct_other = models.FloatField(db_column='PCT_OTHER', blank=True, null=True)  # Field name made lowercase.
    pct_65over = models.FloatField(db_column='PCT_65OVER', blank=True, null=True)  # Field name made lowercase.
    pct_18_64 = models.FloatField(db_column='PCT_18_64', blank=True, null=True)  # Field name made lowercase.
    pct_undr18 = models.FloatField(db_column='PCT_UNDR18', blank=True, null=True)  # Field name made lowercase.
    pct_under5 = models.FloatField(db_column='PCT_UNDER5', blank=True, null=True)  # Field name made lowercase.
    unemployment_rate = models.FloatField(blank=True, null=True)
    n_hospitals = models.FloatField(blank=True, null=True)
    mort_30_ami = models.FloatField(blank=True, null=True)
    mort_30_cabg = models.FloatField(blank=True, null=True)
    mort_30_copd = models.FloatField(blank=True, null=True)
    mort_30_hf = models.FloatField(blank=True, null=True)
    mort_30_pn = models.FloatField(blank=True, null=True)
    mort_30_stk = models.FloatField(blank=True, null=True)
    readm_30_ami = models.FloatField(blank=True, null=True)
    readm_30_cabg = models.FloatField(blank=True, null=True)
    readm_30_copd = models.FloatField(blank=True, null=True)
    readm_30_hf = models.FloatField(blank=True, null=True)
    readm_30_hip_knee = models.FloatField(blank=True, null=True)
    readm_30_hosp_wide = models.FloatField(blank=True, null=True)
    readm_30_pn = models.FloatField(blank=True, null=True)
    readm_30_stk = models.FloatField(blank=True, null=True)
    chlamydia = models.FloatField(db_column='Chlamydia', blank=True, null=True)  # Field name made lowercase.
    tuberculosis = models.FloatField(db_column='Tuberculosis', blank=True, null=True)  # Field name made lowercase.
    gonorrhea = models.FloatField(db_column='Gonorrhea', blank=True, null=True)  # Field name made lowercase.
    hiv = models.FloatField(db_column='HIV', blank=True, null=True)  # Field name made lowercase.
    senior_flu_deaths = models.FloatField(blank=True, null=True)
    measles = models.FloatField(db_column='Measles', blank=True, null=True)  # Field name made lowercase.
    mumps = models.FloatField(db_column='Mumps', blank=True, null=True)  # Field name made lowercase.
    pertussis = models.FloatField(db_column='Pertussis', blank=True, null=True)  # Field name made lowercase.
    rubella = models.FloatField(db_column='Rubella', blank=True, null=True)  # Field name made lowercase.
    varicella_hospitalizations = models.FloatField(blank=True, null=True)
    salmonellosis = models.FloatField(db_column='Salmonellosis', blank=True, null=True)  # Field name made lowercase.
    ecoli_hem = models.FloatField(blank=True, null=True)
    ecoli_nonhem = models.FloatField(blank=True, null=True)
    syphilis = models.FloatField(blank=True, null=True)
    botulism_dtfood = models.FloatField(blank=True, null=True)
    std = models.FloatField(blank=True, null=True)
    vaccine_dx = models.FloatField(blank=True, null=True)
    food_dx = models.FloatField(blank=True, null=True)
    opiods_rx_1000 = models.FloatField(blank=True, null=True)
    opiods_greater_than_stateavg = models.IntegerField(blank=True, null=True)
    milk_price10 = models.FloatField(db_column='MILK_PRICE10', blank=True, null=True)  # Field name made lowercase.
    soda_price10 = models.FloatField(db_column='SODA_PRICE10', blank=True, null=True)  # Field name made lowercase.
    milk_soda_price10 = models.FloatField(db_column='MILK_SODA_PRICE10', blank=True, null=True)  # Field name made lowercase.
    pch_ffr_07_12 = models.FloatField(db_column='PCH_FFR_07_12', blank=True, null=True)  # Field name made lowercase.
    ffr07 = models.FloatField(db_column='FFR07', blank=True, null=True)  # Field name made lowercase.
    ffr12 = models.FloatField(db_column='FFR12', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.county

    class Meta:
        managed = False
        db_table = 'ca_fd'




class Demographic(models.Model):
    state = models.CharField(db_column='State', blank=True, null=True, default='CA', max_length=3)  # Field name made lowercase.
    county = models.TextField(db_column='County', null=False, primary_key=True)  # Field name made lowercase.
    pop2010 = models.FloatField(db_column='POP2010', blank=True, null=True)  # Field name made lowercase.
    num_fd = models.IntegerField(blank=True, null=True)
    pop_in_des = models.FloatField(blank=True, null=True)
    perc_lila = models.FloatField(blank=True, null=True)
    n_tracts = models.FloatField(blank=True, null=True)
    urban_des = models.FloatField(blank=True, null=True)
    rural_des = models.FloatField(blank=True, null=True)
    n_urban = models.FloatField(blank=True, null=True)
    n_rural = models.FloatField(blank=True, null=True)
    des_percent = models.FloatField(blank=True, null=True)
    pct_hspnc = models.FloatField(db_column='PCT_HSPNC', blank=True, null=True)  # Field name made lowercase.
    pct_white = models.FloatField(db_column='PCT_WHITE', blank=True, null=True)  # Field name made lowercase.
    pct_black = models.FloatField(db_column='PCT_BLACK', blank=True, null=True)  # Field name made lowercase.
    pct_asian = models.FloatField(db_column='PCT_ASIAN', blank=True, null=True)  # Field name made lowercase.
    pct_amind_esk = models.FloatField(db_column='PCT_AMIND_ESK', blank=True, null=True)  # Field name made lowercase.
    pct_islander = models.FloatField(db_column='PCT_ISLANDER', blank=True, null=True)  # Field name made lowercase.
    pct_multi = models.FloatField(db_column='PCT_MULTI', blank=True, null=True)  # Field name made lowercase.
    pct_other = models.FloatField(db_column='PCT_OTHER', blank=True, null=True)  # Field name made lowercase.
    pct_65over = models.FloatField(db_column='PCT_65OVER', blank=True, null=True)  # Field name made lowercase.
    pct_18_64 = models.FloatField(db_column='PCT_18_64', blank=True, null=True)  # Field name made lowercase.
    pct_undr18 = models.FloatField(db_column='PCT_UNDR18', blank=True, null=True)  # Field name made lowercase.
    pct_under5 = models.FloatField(db_column='PCT_UNDER5', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.county
    class Meta:
        managed = False
        db_table = 'demographics'


class Infection(models.Model):
    county = models.CharField(db_column='County', blank=True, null=False, primary_key=True, max_length=255)  # Field name made lowercase.
    chlamydia = models.FloatField(db_column='Chlamydia', blank=True, null=True)  # Field name made lowercase.
    tuberculosis = models.FloatField(db_column='Tuberculosis', blank=True, null=True)  # Field name made lowercase.
    gonorrhea = models.FloatField(db_column='Gonorrhea', blank=True, null=True)  # Field name made lowercase.
    hiv = models.FloatField(db_column='HIV', blank=True, null=True)  # Field name made lowercase.
    senior_flu_deaths = models.FloatField(blank=True, null=True)
    measles = models.FloatField(db_column='Measles', blank=True, null=True)  # Field name made lowercase.
    mumps = models.FloatField(db_column='Mumps', blank=True, null=True)  # Field name made lowercase.
    pertussis = models.FloatField(db_column='Pertussis', blank=True, null=True)  # Field name made lowercase.
    rubella = models.FloatField(db_column='Rubella', blank=True, null=True)  # Field name made lowercase.
    varicella_hospitalizations = models.FloatField(blank=True, null=True)
    salmonellosis = models.FloatField(db_column='Salmonellosis', blank=True, null=True)  # Field name made lowercase.
    ecoli_hem = models.FloatField(blank=True, null=True)
    ecoli_nonhem = models.FloatField(blank=True, null=True)
    syphilis = models.FloatField(blank=True, null=True)
    botulism_dtfood = models.FloatField(blank=True, null=True)
    std = models.FloatField(blank=True, null=True)
    vaccine_dx = models.FloatField(blank=True, null=True)
    food_dx = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.county
    class Meta:
        managed = False
        db_table = 'infection'


class Inpatient(models.Model):
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    county = models.TextField(db_column='County', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    pop2010 = models.TextField(db_column='POP2010', blank=True, null=True)  # Field name made lowercase.
    n_hospitals = models.FloatField(blank=True, null=True)
    mort_30_ami = models.FloatField(blank=True, null=True)
    mort_30_cabg = models.FloatField(blank=True, null=True)
    mort_30_copd = models.FloatField(blank=True, null=True)
    mort_30_hf = models.FloatField(blank=True, null=True)
    mort_30_pn = models.FloatField(blank=True, null=True)
    mort_30_stk = models.FloatField(blank=True, null=True)
    readm_30_ami = models.FloatField(blank=True, null=True)
    readm_30_cabg = models.FloatField(blank=True, null=True)
    readm_30_copd = models.FloatField(blank=True, null=True)
    readm_30_hf = models.FloatField(blank=True, null=True)
    readm_30_hip_knee = models.FloatField(blank=True, null=True)
    readm_30_hosp_wide = models.FloatField(blank=True, null=True)
    readm_30_pn = models.FloatField(blank=True, null=True)
    readm_30_stk = models.FloatField(blank=True, null=True)
    chlamydia = models.FloatField(db_column='Chlamydia', blank=True, null=True)  # Field name made lowercase.
    tuberculosis = models.FloatField(db_column='Tuberculosis', blank=True, null=True)  # Field name made lowercase.
    gonorrhea = models.FloatField(db_column='Gonorrhea', blank=True, null=True)  # Field name made lowercase.
    hiv = models.FloatField(db_column='HIV', blank=True, null=True)  # Field name made lowercase.
    senior_flu_deaths = models.FloatField(blank=True, null=True)
    measles = models.FloatField(db_column='Measles', blank=True, null=True)  # Field name made lowercase.
    mumps = models.FloatField(db_column='Mumps', blank=True, null=True)  # Field name made lowercase.
    pertussis = models.FloatField(db_column='Pertussis', blank=True, null=True)  # Field name made lowercase.
    rubella = models.FloatField(db_column='Rubella', blank=True, null=True)  # Field name made lowercase.
    varicella_hospitalizations = models.FloatField(blank=True, null=True)
    salmonellosis = models.FloatField(db_column='Salmonellosis', blank=True, null=True)  # Field name made lowercase.
    ecoli_hem = models.FloatField(blank=True, null=True)
    ecoli_nonhem = models.FloatField(blank=True, null=True)
    syphilis = models.FloatField(blank=True, null=True)
    botulism_dtfood = models.FloatField(blank=True, null=True)
    std = models.FloatField(blank=True, null=True)
    vaccine_dx = models.FloatField(blank=True, null=True)
    food_dx = models.FloatField(blank=True, null=True)
    opiods_rx_1000 = models.FloatField(blank=True, null=True)
    opiods_greater_than_stateavg = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.county
    class Meta:
        managed = False
        db_table = 'inpatient'
