
import requests
import string

from lxml import etree
from lxml import html

from pandas import DataFrame as df
import progressbar

from config_hk_school import *

parser = etree.HTMLParser()

def getSchoolIdList():
    if len(proxies) == 0:
        r = requests.get(school_list_url)
    else:
        r = requests.get(school_list_url, proxies=proxies)
    tree = etree.fromstring(r.content, parser=parser)

    td_list = tree.xpath('//table[@class=\'font_content_school_list\']/tr/td[@onclick]')

    school_id_list = []

    for td in td_list:
        school_id_list.append(td.attrib['onclick'].split('\'')[1])

    return school_id_list


def getSchoolInfo(school_id):
    schoolInfo = dict()
    r = requests.get(school_info_url + school_id.__str__(), proxies=proxies)
    tree = etree.fromstring(r.content, parser=parser)

    district = tree.xpath('//table[@class=\'Font_District_Name\']')[0].getchildren()[1].getchildren()[1].text.strip()

    basicInfoNode = tree.xpath('//table[@class=\'font_content_schoolinfo\']')
    school_name = basicInfoNode[0].getchildren()[0].getchildren()[0].text.strip()
    school_addr = basicInfoNode[0].getchildren()[2].getchildren()[1].text.strip()
    school_tel = basicInfoNode[0].getchildren()[4].getchildren()[1].text.strip()
    school_fax = basicInfoNode[0].getchildren()[6].getchildren()[1].text.strip()

    moreInfoNode = tree.xpath('//table[@class=\'font_content_box\']')
    school_year = moreInfoNode[2].getchildren()[0].getchildren()[0].text.strip()
    voucher = moreInfoNode[2].getchildren()[1].getchildren()[1].text.strip()

    school_cat = moreInfoNode[3].getchildren()[0].getchildren()[1].text.strip()
    student_cat = moreInfoNode[3].getchildren()[1].getchildren()[1].text.strip()
    supervisor = moreInfoNode[3].getchildren()[2].getchildren()[1].text.strip()
    principal = moreInfoNode[3].getchildren()[3].getchildren()[1].text.strip()
    found_year = moreInfoNode[3].getchildren()[4].getchildren()[1].text.strip()
    accomodation = moreInfoNode[3].getchildren()[5].getchildren()[1].text.strip()
    num_of_classrm = moreInfoNode[3].getchildren()[6].getchildren()[1].text.strip()
    outdoor_playground = moreInfoNode[3].getchildren()[7].getchildren()[1].text.strip()
    indoor_playground = moreInfoNode[3].getchildren()[8].getchildren()[1].text.strip()
    music_rm = moreInfoNode[3].getchildren()[9].getchildren()[1].text.strip()
    other_rm = moreInfoNode[3].getchildren()[10].getchildren()[1].text.strip()
    num_of_teacher = moreInfoNode[3].getchildren()[11].getchildren()[1].text.strip()
    try:
        website = moreInfoNode[3].getchildren()[12].getchildren()[1].getchildren()[0].text.strip()
    except IndexError:
        website = moreInfoNode[3].getchildren()[12].getchildren()[1].text.strip()
    try:
        quality_review_result = moreInfoNode[3].getchildren()[13].getchildren()[1].text.strip()
        quality_review_report = moreInfoNode[3].getchildren()[13].getchildren()[1].getchildren()[0].text.strip()
    except IndexError:
        quality_review_result = 'N/A'
        quality_review_report = 'N/A'

    degree_holder = moreInfoNode[4].getchildren()[1].getchildren()[1].text.strip()
    non_degree_holder = moreInfoNode[4].getchildren()[2].getchildren()[1].text.strip()
    ece_cert = moreInfoNode[4].getchildren()[4].getchildren()[1].text.strip()
    kg_teacher = moreInfoNode[4].getchildren()[5].getchildren()[1].text.strip()
    other_teacher_training = moreInfoNode[4].getchildren()[6].getchildren()[1].text.strip()
    asist_kg_teacher = moreInfoNode[4].getchildren()[7].getchildren()[1].text.strip()
    other_qual = moreInfoNode[4].getchildren()[8].getchildren()[1].text.strip()

    am_teacher_ratio = moreInfoNode[6].getchildren()[1].text.strip()
    pm_teacher_ratio = moreInfoNode[6].getchildren()[2].getchildren()[1].text.strip()
    incld_age_2_3 = moreInfoNode[6].getchildren()[3].getchildren()[1].text.strip()

    am_n = moreInfoNode[7].getchildren()[1].getchildren()[1].text.strip()
    am_low_kg = moreInfoNode[7].getchildren()[1].getchildren()[2].text.strip()
    am_up_kg = moreInfoNode[7].getchildren()[1].getchildren()[3].text.strip()
    pm_n = moreInfoNode[7].getchildren()[2].getchildren()[1].text.strip()
    pm_low_kg = moreInfoNode[7].getchildren()[2].getchildren()[2].text.strip()
    pm_up_kg = moreInfoNode[7].getchildren()[2].getchildren()[3].text.strip()
    wd_n = moreInfoNode[7].getchildren()[3].getchildren()[1].text.strip()
    wd_low_kg = moreInfoNode[7].getchildren()[3].getchildren()[2].text.strip()
    wd_up_kg = moreInfoNode[7].getchildren()[3].getchildren()[3].text.strip()

    fee_am_n = moreInfoNode[8].getchildren()[1].getchildren()[2].text.strip()
    fee_am_low_kg = moreInfoNode[8].getchildren()[1].getchildren()[3].text.strip()
    fee_am_up_kg = moreInfoNode[8].getchildren()[1].getchildren()[4].text.strip()
    fee_pm_n = moreInfoNode[8].getchildren()[2].getchildren()[1].text.strip()
    fee_pm_low_kg = moreInfoNode[8].getchildren()[2].getchildren()[2].text.strip()
    fee_pm_up_kg = moreInfoNode[8].getchildren()[2].getchildren()[3].text.strip()
    fee_wd_n = moreInfoNode[8].getchildren()[3].getchildren()[1].text.strip()
    fee_wd_low_kg = moreInfoNode[8].getchildren()[3].getchildren()[2].text.strip()
    fee_wd_up_kg = moreInfoNode[8].getchildren()[3].getchildren()[3].text.strip()
    try:
        red_fee_am_n = moreInfoNode[8].getchildren()[5].getchildren()[2].text.strip()
        red_fee_am_low_kg = moreInfoNode[8].getchildren()[5].getchildren()[3].text.strip()
        red_fee_am_up_kg = moreInfoNode[8].getchildren()[5].getchildren()[4].text.strip()
        red_fee_pm_n = moreInfoNode[8].getchildren()[6].getchildren()[1].text.strip()
        red_fee_pm_low_kg = moreInfoNode[8].getchildren()[6].getchildren()[2].text.strip()
        red_fee_pm_up_kg = moreInfoNode[8].getchildren()[6].getchildren()[3].text.strip()
        red_fee_wd_n = moreInfoNode[8].getchildren()[7].getchildren()[1].text.strip()
        red_fee_wd_low_kg = moreInfoNode[8].getchildren()[7].getchildren()[2].text.strip()
        red_fee_wd_up_kg = moreInfoNode[8].getchildren()[7].getchildren()[3].text.strip()
    except IndexError:
        red_fee_am_n = 'N/A'
        red_fee_am_low_kg = 'N/A'
        red_fee_am_up_kg = 'N/A'
        red_fee_pm_n = 'N/A'
        red_fee_pm_low_kg = 'N/A'
        red_fee_pm_up_kg = 'N/A'
        red_fee_wd_n = 'N/A'
        red_fee_wd_low_kg = 'N/A'
        red_fee_wd_up_kg = 'N/A'

    child_care_serv = moreInfoNode[10].getchildren()[0].getchildren()[1].text.strip()
    fee_child_care_hd = moreInfoNode[10].getchildren()[2].getchildren()[0].text.strip()
    fee_child_care_wd = moreInfoNode[10].getchildren()[2].getchildren()[1].text.strip()
    child_care_under_2 = moreInfoNode[10].getchildren()[3].getchildren()[1].text.strip()
    num_of_2_3 = moreInfoNode[10].getchildren()[4].getchildren()[1].text.strip()
    child_care_subsidy = moreInfoNode[10].getchildren()[5].getchildren()[1].text.strip()
    occasional_child_care = moreInfoNode[10].getchildren()[6].getchildren()[1].text.strip()
    extend_hour = moreInfoNode[10].getchildren()[7].getchildren()[1].text.strip()

    curriculum = moreInfoNode[11].getchildren()[1].getchildren()[1].text.strip()

    summer_uni = moreInfoNode[13].getchildren()[1].getchildren()[1].text.strip()
    winter_uni = moreInfoNode[13].getchildren()[1].getchildren()[3].text.strip()
    school_bag = moreInfoNode[13].getchildren()[2].getchildren()[1].text.strip()
    snack = moreInfoNode[13].getchildren()[2].getchildren()[3].text.strip()
    txt_book = moreInfoNode[13].getchildren()[3].getchildren()[1].text.strip()
    exe_book = moreInfoNode[13].getchildren()[3].getchildren()[3].text.strip()

    app_form = moreInfoNode[17].getchildren()[1].getchildren()[1].text.strip()
    app_period = moreInfoNode[17].getchildren()[2].getchildren()[1].text.strip()

    app_fee = moreInfoNode[18].getchildren()[1].getchildren()[1].text.strip()
    reg_fee_hd = moreInfoNode[18].getchildren()[2].getchildren()[2].text.strip()
    reg_fee_wd = moreInfoNode[18].getchildren()[3].getchildren()[1].text.strip()

    schoolInfo = {'school_id': school_id, 'district' : district, 'school_name': school_name, 'school_addr': school_addr, 'school_tel': school_tel,
                  'school_fax': school_fax,
                  'school_year': school_year, 'voucher': voucher, 'school_cat': school_cat, 'student_cat': student_cat, 'supervisor': supervisor,
                  'principal': principal, 'found_year': found_year, 'accomodation': accomodation, 'num_of_classrm': num_of_classrm,
                  'outdoor_playground': outdoor_playground, 'indoor_playground': indoor_playground, 'music_rm': music_rm,
                  'other_rm': other_rm, 'num_of_teacher': num_of_teacher, 'website': website, 'quality_review_result': quality_review_result,
                  'quality_review_report': quality_review_report, 'degree_holder': degree_holder, 'non_degree_holder': non_degree_holder,
                  'ece_cert': ece_cert, 'kg_teacher': kg_teacher, 'other_teacher_training': other_teacher_training, 'asist_kg_teacher': asist_kg_teacher,
                  'other_qual': other_qual, 'am_teacher_ratio': am_teacher_ratio, 'pm_teacher_ratio': pm_teacher_ratio, 'incld_age_2_3': incld_age_2_3,
                  'am_n': am_n, 'am_low_kg': am_low_kg, 'am_up_kg': am_up_kg, 'pm_n': pm_n, 'pm_low_kg': pm_low_kg, 'pm_up_kg': pm_up_kg,
                  'wd_n': wd_n, 'wd_low_kg': wd_low_kg, 'wd_up_kg': wd_up_kg, 'fee_am_n': fee_am_n, 'fee_am_low_kg': fee_am_low_kg,
                  'fee_am_up_kg': fee_am_up_kg, 'fee_pm_n': fee_pm_n, 'fee_pm_low_kg': fee_pm_low_kg, 'fee_pm_up_kg': fee_pm_up_kg,
                  'fee_wd_n': fee_wd_n, 'fee_wd_low_kg': fee_wd_low_kg, 'fee_wd_up_kg': fee_wd_up_kg, 'red_fee_am_n': red_fee_am_n,
                  'red_fee_am_low_kg': red_fee_am_low_kg, 'red_fee_am_up_kg': red_fee_am_up_kg, 'red_fee_pm_n': red_fee_pm_n,
                  'red_fee_pm_low_kg': red_fee_pm_low_kg, 'red_fee_pm_up_kg': red_fee_pm_up_kg, 'red_fee_wd_n': red_fee_wd_n,
                  'red_fee_wd_low_kg': red_fee_wd_low_kg, 'red_fee_wd_up_kg': red_fee_wd_up_kg, 'child_care_serv': child_care_serv,
                  'fee_child_care_hd': fee_child_care_hd, 'fee_child_care_wd': fee_child_care_wd, 'child_care_under_2': child_care_under_2,
                  'num_of_2_3': num_of_2_3, 'child_care_subsidy': child_care_subsidy, 'occasional_child_care': occasional_child_care,
                  'extend_hour': extend_hour, 'curriculum': curriculum, 'summer_uni': summer_uni, 'winter_uni': winter_uni, 'txt_book': txt_book,
                  'exe_book': exe_book, 'school_bag': school_bag, 'snack': snack, 'app_form': app_form, 'app_period': app_period, 'app_fee': app_fee,
                  'reg_fee_hd': reg_fee_hd, 'reg_fee_wd': reg_fee_wd}

    return schoolInfo

def constructSchoolDF():

    school_id_list = getSchoolIdList()
    schoolInfoData = []

    num_of_id = len(school_id_list)

    with progressbar.ProgressBar(max_value=num_of_id) as bar:
        for idx, school_id in enumerate(school_id_list):
            # print('processing school #' + (idx + 1).__str__() + '. school ID: ' + school_id.__str__())
            schoolInfoData.append(getSchoolInfo(school_id))
            bar.update(idx + 1)
            # clear_output()

    df_schoolInfo = df(schoolInfoData).reindex(columns=['school_id', 'district', 'school_name', 'school_addr', 'school_tel', 'school_fax', 'school_year', 'voucher',
                                              'school_cat', 'student_cat', 'supervisor', 'principal', 'found_year', 'accomodation', 'num_of_classrm', 'outdoor_playground',
                                              'indoor_playground', 'music_rm', 'other_rm', 'num_of_teacher', 'website', 'quality_review_result', 'quality_review_report',
                                              'degree_holder', 'non_degree_holder', 'ece_cert', 'kg_teacher', 'other_teacher_training', 'asist_kg_teacher', 'other_qual',
                                              'am_teacher_ratio', 'pm_teacher_ratio', 'incld_age_2_3', 'am_n', 'am_low_kg', 'am_up_kg', 'pm_n', 'pm_low_kg', 'pm_up_kg',
                                              'wd_n', 'wd_low_kg', 'wd_up_kg', 'fee_am_n', 'fee_am_low_kg', 'fee_am_up_kg', 'fee_pm_n', 'fee_pm_low_kg', 'fee_pm_up_kg',
                                              'fee_wd_n', 'fee_wd_low_kg', 'fee_wd_up_kg', 'red_fee_am_n', 'red_fee_am_low_kg', 'red_fee_am_up_kg', 'red_fee_pm_n',
                                              'red_fee_pm_low_kg', 'red_fee_pm_up_kg', 'red_fee_wd_n', 'red_fee_wd_low_kg', 'red_fee_wd_up_kg', 'child_care_serv',
                                              'fee_child_care_hd', 'fee_child_care_wd', 'child_care_under_2', 'num_of_2_3', 'child_care_subsidy', 'occasional_child_care',
                                              'extend_hour', 'curriculum', 'summer_uni', 'winter_uni', 'txt_book', 'exe_book', 'school_bag', 'snack', 'app_form',
                                               'app_period', 'app_fee', 'reg_fee_hd', 'reg_fee_wd'])

    df_schoolInfo.columns = ['school_id', '地區', '學校名稱', '地址', '電話', 'FAX', '學年', '學券資格', '學校類別',
                             '學生類別', '校監', '校長', '創校年份', '課室的總容額', '課室數目', '戶外遊戲場地',
                             '室內遊戲場地', '音樂室', '其他特別室', '教學人員總人數', 'website', '質素評核結果', '質素評核報告',
                             '持有學位教員', '非持有學位教員', '幼兒教育證書教員', '幼稚園教師教員', '其他師資訓練教員', '助理幼稚園教師教員', '其他教員',
                             '上午班師生比例', '下午班師生比例', '師生比例包括N班', '上午N班人數', '上午低班人數', '上午高班人數', '下午N班人數', '下午低班人數',
                             '下午高班人數',
                             '全日N班人數', '全日低班人數', '全日高班人數', '上午N班學費', '上午低班學費', '上午高班學費', '下午N班學費', '下午低班學費',
                             '下午高班學費',
                             '全日N班學費', '全日低班學費', '全日高班學費', '上午N班用學劵', '上午低班用學劵', '上午高班用學劵', '下午N班用學劵',
                             '下午低班用學劵', '下午高班用學劵', '全日N班用學劵', '全日低班用學劵', '全日高班用學劵', '2-3歲幼兒服務',
                             '半日幼兒服務收費', '全日幼兒服務收費', '2歲以下幼兒服務', '2-3歲級別兒童人數', '幼兒中心資助計劃', '暫托服務',
                             '延長服務時間', '課程類別', '夏季校服', '冬季校服', '課本', '練習簿', '書包', '茶點', '申請表格',
                             '請日期', '報名費', '半日班註冊費', '全日班註冊費']

    return df_schoolInfo