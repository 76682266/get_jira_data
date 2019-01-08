# -*- coding: utf-8 -*-
#list the single or team jql of abilities
'''
read https://kms.finedevelop.com/pages/viewpage.action?pageId=46744701
能力后面的_11_12代表了几月份,人工录入的放在judge_ability上面,如果是写在single或者team里面但是没写语句的,则为未获取
ab1:1.a 责任客户bug
ab2:1.b 被退回的开发测试任务
ab3:1.f 快速任务质量情况
ab4:2.e 日志情况，可以认为是个执行力，需要结合ellen的取数来算,暂且先不算了
ab5:3.a 提交的已解决的bug
ab6:3.d 文档分享分数,需要人工录入
ab7:4.a 执行扣分,需要人工录入
1.g 累计提交的已解决的开发测试任务

teamab:
ab1:1.c 产品线的责任客户BUG
ab2:3.c 退回的客户BUG
ab3:3.f 版本发布的数量,需要人工计算

能力为空则不会进行取数
'''
team_config={
    #控制每个组要搜索哪些能力
    '图表':['chart_1.c','chart_3.c'],
    '平台':['dec_1.c','dec_3.c'],
    'FR-移动端':['mobile_1.c','mobile_3.c'],
    'BI-移动端':['mobile_1.c','mobile_3.c'],
    'BI-直连':['bi_1.c','bi_3.c'],
    'BI-数据挖掘':['bi_1.c','bi_3.c'],
    'BI-cube':['bi_1.c','bi_3.c'],
    'FR-设计器':['fr_1.c','fr_3.c'],
    '测试开发':['']

}

single_ab_201811_201812={
    '1.a':'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 客户BUG AND created >= 2018-11-1 AND created <= 2018-12-31 AND NOT (问题解决方案 is not EMPTY AND 问题解决方案 in (不是bug, 需求处理, 文档优化, 永不修复, 产品改进) AND status in (创建者确认, 被否决)) AND NOT (问题解决方案 is not EMPTY AND 问题解决方案 in (重复BUG) AND status in (创建者验收, 创建者确认, 被否决, 已解决, 验收通过待发布, 产品场景确认)) AND (分支 = MASTER稳定版 OR 分支 is EMPTY) AND NOT status in (重复BUG待解决) AND 责任测试 = ',
    '1.b':'project in (BI, DEC, CHART, REPORT, MOBILE) AND issuetype = 开发测试任务 AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 研发退回原因 in (不是BUG) AND reporter = ',
    '1.f': '',
    '2.e': '',
    '3.a': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND (resolved >= 2018-11-01 AND resolved <= 2018-12-31) AND reporter = ',
    '1.g': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND reporter = '


}
team_ab_201811_201812={
    'chart_1.c':'(filter = 13045 AND component in (报表图表, 扩展图表) OR filter = 13046 AND component in (BI图表, 图表)) AND created >= 2018-11-01 AND created <= 2018-12-31',
    'chart_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'dec_1.c':'filter=12925  AND created >= 2018-11-01 AND created <= 2018-12-31',
    'dec_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby)',
    'mobile_1.c':'filter=12924 AND created >= 2018-11-01 AND created <= 2018-12-31',
    'mobile_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda)',
    'bi_1.c':'filter=13046 AND created >= 2018-11-01 AND created <= 2018-12-31 AND project != 决策平台 AND component in(X引擎,集群,性能,BI后端,BI前端)',
    'bi_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (panda,haya,jiangfeng,paul.zhang,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'fr_1.c':'filter=13045 AND created >= 2018-11-01 AND created <= 2018-12-31 AND component in (基础框架,数据源,swift,云端,x引擎,报表功能,填报,官方插件,计算引擎)',
    'fr_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo)'

}

judge_ab_201811_201812={
    'Neo.Zhu':{'3.d':'162.5'},
    'Alisa':{'3.d':'91.8'},
    'jeo':{'3.d':'84.7'},
    'Lipei':{'3.d':'134.4'},
    'panda':{'3.d':'118'},
    'paul':{'3.d':'170.5'}
}
