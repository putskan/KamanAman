import os

KAMANIM_SQLITE_DB_PATH = 'sqlite:///db/kamanim.db'
WORKING_DIR = os.path.dirname(__file__)
REPORTS_PATH = os.path.join(WORKING_DIR, 'reports/')
######################################################
################### Email  Related ###################
SENDER_PASSWORD_PATH = os.path.join(WORKING_DIR, "email_pass")
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "kamanaman101@gmail.com"
RECIEVER_EMAIL = "kamanaman101@gmail.com"
EMAIL_PORT = 587
######################################################
####################### Regex ########################
LINK_ENGLISH_INPUT_NAME_TO_HEBREW_DESCRIPTION_REGEX = r'<label.*?>(.*?)</.*?\n.*?type="(?!radio).*?name="(.*?)"|<label.*?>(.*?)</.*?\n.*?textarea.*?name="(.*?)"|<div.*?>(.*?)</.*?\n.*type="radio".*?name="(.*?)"'
DATE_REGEX = r"^\d{4}-[0-1]\d-[0-3]\d$"
######################################################
# used for identifying which table to add the POST data to
fe_to_be_tbl_identifier = {'akasjdhkah': 'Medical'}

# used to insert data to Medical tbl - Currently not used
MEDICAL_TABLE_EMPTY_DICT = {
'private_number': '',
'citizen_id': '',
'full_name': '',
'medical_profile': '',
'height': '',
'weight': '',
'drug_sensitivity': '',
'drug_sensitivity_details': '',
'smoking': '',
'surgery': '',
'surgery_details': '',
'intrusive_treatment': '',
'intrusive_treatment_details': '',
'eye_surgery': '',
'eye_surgery_details': '',
'recommended_surgery': '',
'recommended_surgery_details': '',
'recommended_surgery_incompletion_reason': '',
'repeating_sprains': '',
'current_week_sprains': '',
'last_year_sprains': '',
'current_walking_disablity': '',
'current_walking_disablity_details': '',
'head_injury': '',
'head_injury_when': '',
'head_injury_after_tzav_rishon': '',
'head_injury_supervision_or_problem': '',
'repeating_headaches': '',
'headaches_in_last_half_year': '',
'headaches_should_see_doctor': '',
'headaches_previous_checks': '',
'headaches_diagnosis': '',
'headaches_waking_up': '',
'headaches_with_blurred_vision': '',
'headaches_with_morning_vomit': '',
'frequent_faintings': '',
'fainting_during_exercise': '',
'fainting_after_exercise': '',
'faintings_in_last_year': '',
'faintings_previous_checks': '',
'faintings_additional_info': '',
'hearing_problems': '',
'hearing_problems_details': '',
'repeating_eye_inflammation': '',
'currently_with_eye_inflammation': '',
'eye_inflammation_routine_treatment': '',
'chest_pain': '',
'chest_pain_from_exercise': '',
'is_chest_pain_limiting': '',
'chest_pain_previous_checks': '',
'chest_pain_previous_checks_details': '',
'arrhythmia': '',
'arrhythmia_in_exercise': '',
'arrhythmia_previous_checks': '',
'arrhythmia_previous_checks_details': '',
'asthma': '',
'asthma_hospital_admission': '',
'asthma_recent_deterioration': '',
'asthma_enough_inhalers': '',
'asthma_deterioration_since_profile_determination': '',
'breathing_problems': '',
'breathing_problems_previous_checks': '',
'breathing_problems_details': '',
'continious_backaches': '',
'are_continious_backaches_new': '',
'continious_backaches_with_weight_loss': '',
'continious_backaches_with_night_sweat': '',
'continious_backaches_previous_checks': '',
'continious_backaches_details': '',
'skin_diseases': '',
'skin_diseases_currently_treated': '',
'skin_diseases_currently_treated_details': '',
'skin_diseases_taking_rakotan': '',
'crotch_issues': '',
'crotch_issues_type': '',
'crotch_issues_previous_checks': '',
'crotch_issues_details': '',
'meniscus_or_band_issues': '',
'meniscus_or_band_issues_restrict_functioning': '',
'meniscus_or_band_issues_diagnosed_after_profile_determined': '',
'stomachaches_or_diarrhea': '',
'unusual_stomachaches': '',
'diarrhea_for_over_a_week': '',
'diarrhea_with_blood_or_saliva': '',
'stomachaches_or_diarrhea_with_fever': '',
'stomachaches_or_diarrhea_back_from_abroad': '',
'diarrhea_people_around_you': '',
'stomachaches_or_diarrhea_weight_loss': '',
'stomachaches_or_toilet_traffic_change': '',
'stomachaches_or_diarrhea_vomit': '',
'stomachaches_or_diarrhea_previous_checks': '',
'stomachaches_or_diarrhea_details': '',
'weight_loss_5kg_6mo': '',
'weight_loss_5kg_6mo_intentional': '',
'heat_injury': '',
'heat_injury_details': '',
'psycho_treatment': '',
'psycho_treatment_details': '',
'psycho_treatment_continue_with_idf': '',
'psycho_issue': '',
'psycho_issue_details': '',
'last_3yr_hospitalization': '',
'last_3yr_hospitalization_details': '',
'other_medical_issue': '',
'other_medical_issue_details': '',
'relaxation_sleep_drugs': '',
'relaxation_sleep_drugs_details': '',
'enough_relaxation_sleep_drugs': '',
'alcohol_consumption': '',
'alcohol_consumption_details': '',
'other_drugs_consumption': '',
'other_drugs_consumption_details': '',
'enough_of_other_drugs': '',
'food_allergies': '',
'food_allergies_details': '',
'epipen': '',
'ventolin': '',
'is_ventolin_epipen_missing': '',
'missing_ventolin_epipen_type': '',
'epilepsy': '',
'epilepsy_is_medically_treated': '',
'epilepsy_last_seizure_date': '',
'epilepsy_details': '',
'epilepsy_is_medically_treated_and_missing': '',
'epilepsy_is_medically_treated_and_missing_details': '',
'relative_death_before_50': '',
'relative_death_before_50_details': '',
'cancer_in_family': '',
'cancer_in_family_details': '',
'last_week_fever': '',
'last_week_fever_healed': '',
'last_week_diarrhea_vomit_stomachache': '',
'last_week_diarrhea_vomit_stomachache_healed': '',
'currently_using_drugs': '',
'currently_using_drugs_details': '',
'currently_under_supervision': '',
'currently_under_supervision_details': '',
}
