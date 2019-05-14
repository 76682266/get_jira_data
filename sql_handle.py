# -*- coding: utf-8 -*-
import pymysql
from config import jira_url,jira_user,jira_passwd
#provide ways to get sql or write sql
#use sql insert update exp↓
# INSERT INTO `量化数据` ( `姓名`, `年月日`, `1.a` )
# VALUES
# 	( 'Panda', '2018-09-01', 25 )
# 	ON DUPLICATE KEY UPDATE `1.a` =
# VALUES
# 	( `1.a` )
def get_members():
    connection = pymysql.connect(host=jira_url,
                                 user=jira_user,
                                 password=jira_passwd,
                                 db='TestGroup',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql_str="SELECT `产品线标签` AS team,GROUP_CONCAT(DISTINCT `user_username`) AS name,`定位` AS job FROM `人员信息表格` GROUP BY `user_username`;"
            #print (sql_str)
            cursor.execute(sql_str)
            result = cursor.fetchall()
            members = {}
            for dict in result:
                if dict['name'] not in members.keys():
                    members[dict['name']]={'team':dict['team'],'job':dict['job']}
            import json
            with open('members.json', 'w') as file:
                file.write(json.dumps(members,ensure_ascii=False))
            #print(type(members))
            #return a list
            #return members
    finally:
        connection.close()
def get_result(sql_str):
    #use you own config.py
    connection = pymysql.connect(host=jira_url,
                                 user=jira_user,
                                 password=jira_passwd,
                                 db='TestGroup',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "SELECT `产品模块`,`姓名`,`角色` FROM `月评表_seven_评价为数字`"
            cursor.execute(sql_str)
            result = cursor.fetchall()
            #return a list
            return result
    finally:
        connection.close()

def write_string(name,datetime,value_dict):
    connection = pymysql.connect(host=jira_url,
                                 user=jira_user,
                                 password=jira_passwd,
                                 db='TestGroup',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    COLstr = ''  # 列的字段拼接
    ROWstr = ''  # 行字段拼接
    SETstr = ''  #UPDATE字段拼接
    for key in value_dict.keys():
        COLstr = COLstr + '`' + key +'`' ','
        ROWstr = (ROWstr +"'"+ '%s'+"'" + ',') % (value_dict[key])
        SETstr = SETstr+'`%s`=VALUES(`%s`)' %(key,key)+','
    SETstr=SETstr.rstrip(",")+";" #由于要收尾，要再处理下分号
    #print(COLstr)
    #print(ROWstr)
    #print(SETstr)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `量化数据` (`姓名`,`年月日`,%s) VALUES('%s','%s',%s) ON DUPLICATE KEY UPDATE %s"%(COLstr[:-1],name,datetime,ROWstr[:-1],SETstr)
            #print(sql)
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()
    print('%s %s的能力取数更新成功' %(name,datetime))

if __name__ == '__main__':
    get_members()
    pass
    #str="SELECT `产品模块`,`姓名`,`角色` FROM `月评表_seven_评价为数字`"
    #print(get_result(str))
    #write_string('panda','2018-08-01',{'1.a':'50','1.b':'20','1.c':'11'})
