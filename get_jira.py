# coding:utf=8
import json
import time
from jira import JIRA
from config import url,user,passwd
from sql_handle import get_result,write_string
#from ability import single_ab_201811_201812,team_ab_201811_201812
jira = JIRA(url, basic_auth=(user, passwd))
#use you own config.py
#demo : result=jira.search_issues(jql3,json_result=True)
# print (type(result)) == dict
# print(result['total'])  #calc num
# print (result) # the details
def get_ab_common(sql):
    # 注意下有些需要传递name 拼接下sql语句
    #print(sql)
    result = jira.search_issues(sql, json_result=True)
    return str(result['total'])  # int2str

# class JIRA_PERSON():
#     #定义下每个人基础的属性，这样的话就可以每次根据这个人的情况去获取对应的数值
#     #基础属性
#     def __init__(self, name,team,job):
#         #name:英文名字 team：产品线 job：职位（比如组长，组员，测开组长，测开组员）
#         self.name = name
#         self.team = team
#         self.job = job
#
#     def get_ab_common(self,sql):
#         #注意下有些需要传递name 拼接下sql语句
#         result=jira.search_issues(sql,json_result=True)
#         return str(result['total']) #int to str


# miley=JIRA_PERSON('miley','BI-移动端','组长')
# miley_dict={}
# print (miley.name,miley.team,miley.job)
# print(miley.get_ab_common(single_ab_201811_201812['ab1']+miley.name))
# print(miley.get_ab_common(single_ab_201811_201812['ab2']+miley.name))
# print(miley.get_ab_common(single_ab_201811_201812['ab5']+miley.name))
# print(miley.get_ab_common(team_ab_201811_201812['chart_ab1']))

def get_result(month="2018-11-01",person=[]):
    #get single ability and team ability
    exact_dict={}
    if month=="2018-11-01":
        from ability import single_ab_201811_201812 as single,team_config,team_ab_201811_201812 as team,judge_ab_201811_201812 as judge  #single is a dict
    if month=="2019-01-01":
        from ability import single_ab_201901_201902 as single,team_config,team_ab_201901_201902 as team,judge_ab_201901_201902 as judge  #single is a dict
    with open('members.json', 'r') as members_json:
        members_dict = json.load(members_json) #a dict
        if len(person):
            #这里指定了要获取的人的字典
            for x in person:
                exact_dict[x]=members_dict[x]
            members_dict=exact_dict
            #print(members_dict)

    for key,value in members_dict.items():
        #value is also a dict,key is a str
        ab={} #to store the ability as a dict
        if key in judge.keys():
            for judge_ab,judge_value in judge[key].items():
                ab[judge_ab]=judge_value
        for ab_name,ab_jql in single.items():
            #print(ab_name,ab_jql,len(ab_jql))
            if len(ab_jql):
                ab[ab_name]=get_ab_common((ab_jql+'"'+key+'"'))
            else:
                ab[ab_name]=''
            time.sleep(0.5)

        for i in team_config[value['team']]:
            if len(i):
                if len(team[i]):
                    ab[i.rsplit('_')[-1]]=get_ab_common(team[i])
                else:
                    ab[i.rsplit('_')[-1]]=''
                time.sleep(0.5)
        if len(ab):
            members_dict[key][month] = ab
            write_string(key, month, ab)
            print('%s:属于%s,职位为%s,%s的能力值为%s' %(key,value['team'],value['job'],month,str(ab)))
    #print(type(members_dict))
    #print(members_dict)
if __name__ == '__main__':
    get_result(month="2019-01-01")
    #jql=single_ab_201811_201812['1.f']+'Abbie'
    #print(get_ab_common(jql))
