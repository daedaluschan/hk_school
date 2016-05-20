from school_web_scrap import *

df_schoolInfo = constructSchoolDF()
df_schoolInfo.to_csv('kg_school_info.csv', sep='|')
