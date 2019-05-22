# -*- coding: utf-8 -*-
#list the single or team jql of abilities
'''
read https://kms.finedevelop.com/pages/viewpage.action?pageId=46744701
能力后面的_11_12代表了几月份,人工录入的放在judge_ability上面,如果是写在single或者team里面但是没写语句的,则为未获取
在用 1.a 责任客户bug
在用 1.b 被退回的开发测试任务
1.f 快速任务质量情况
2.e 日志情况，可以认为是个执行力，需要结合ellen的取数来算,暂且先不算了
在用 3.a 提交的已解决的bug,必须是解决时间在这个时间段内的
在用 3.b 周期内创建的开发测试BUG,不需要算解决
3.d 文档分享分数,需要人工录入
4.a 执行扣分,需要人工录入
1.g 累计提交的已解决的开发测试任务
1.h 个人累计创建的开发测试任务

teamab:
1.c 产品线的责任客户BUG
3.c 退回的客户BUG
3.f 版本发布贡献分值,需要人工计算
在用 5.b 该小组创建的开发测试BUG
在用 5.c 小组创建并解决的开发测试BUG

能力为空则不会进行取数
'''
team_config_old={
    #控制每个组要搜索哪些能力
    '图表':['chart_1.c','chart_3.c','chart_5.b','chart_5.c'],
    '平台':['dec_1.c','dec_3.c','dec_5.b','dec_5.c'],
    'FR-移动端':['mobile_1.c','mobile_3.c','mobile_5.b','mobile_5.c'],
    'BI-移动端':['mobile_1.c','mobile_3.c','mobile_5.b','mobile_5.c'],
    'BI-直连':['bi_1.c','bi_3.c','bi_5.b','bi_5.c'],
    'BI-数据挖掘':['bi_1.c','bi_3.c','bi_5.b','bi_5.c'],
    'BI-cube':['bi_1.c','bi_3.c','bi_5.b','bi_5.c'],
    'FR-设计器':['fr_1.c','fr_3.c','fr_5.b','fr_5.c'],
    '测试开发':['sdet_5.b','sdet_5.c']

}
team_config={
    #控制每个组要搜索哪些能力
    'CHART':['chart_1.c','chart_3.c','chart_5.b','chart_5.c'],
    'DEC':['dec_1.c','dec_3.c','dec_5.b','dec_5.c'],
    'MOBILE':['mobile_1.c','mobile_3.c','mobile_5.b','mobile_5.c'],
    'BI':['bi_1.c','bi_3.c','bi_5.b','bi_5.c'],
    'REPORT':['fr_1.c','fr_3.c','fr_5.b','fr_5.c'],
    'SDET':['sdet_5.b','sdet_5.c']

}

single_ab_201811_201812={
    '1.a':'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 客户BUG AND created >= 2018-11-1 AND created <= 2018-12-31 AND NOT (问题解决方案 is not EMPTY AND 问题解决方案 in (不是bug, 需求处理, 文档优化, 永不修复, 产品改进) AND status in (创建者确认, 被否决)) AND NOT (问题解决方案 is not EMPTY AND 问题解决方案 in (重复BUG) AND status in (创建者验收, 创建者确认, 被否决, 已解决, 验收通过待发布, 产品场景确认)) AND (分支 = MASTER稳定版 OR 分支 is EMPTY) AND NOT status in (重复BUG待解决) AND 责任测试 = ',
    '1.b':'project in (BI, DEC, CHART, REPORT, MOBILE) AND issuetype = 开发测试任务 AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 研发退回原因 in (不是BUG) AND reporter = ',
    '1.f': '',
    '2.e': '',
    '3.a': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND (resolved >= 2018-11-01 AND resolved <= 2018-12-31) AND reporter = ',
    '3.b': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND (created >= 2018-11-01 AND created <= 2018-12-31) AND reporter = ',
    '1.g': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND reporter = ',
    '1.h':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND reporter = '

}
team_ab_201811_201812={
    'chart_1.c':'(filter = 13045 AND component in (报表图表, 扩展图表) OR filter = 13046 AND component in (BI图表, 图表)) AND created >= 2018-11-01 AND created <= 2018-12-31',
    'chart_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'chart_5.b': 'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'chart_5.c': 'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'dec_1.c':'filter=12925  AND created >= 2018-11-01 AND created <= 2018-12-31',
    'dec_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby)',
    'dec_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby)',
    'dec_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby)',
    'mobile_1.c':'filter=12924 AND created >= 2018-11-01 AND created <= 2018-12-31',
    'mobile_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,luna,lioucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'mobile_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,Chanda,luna,lioucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'mobile_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,Chanda,luna,lioucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'bi_1.c':'filter=13046 AND created >= 2018-11-01 AND created <= 2018-12-31 AND project != 决策平台 AND component in(X引擎,集群,性能,BI后端,BI前端)',
    'bi_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (panda,haya,jiangfeng,paul.zhang,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'bi_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (panda,haya,jiangfeng,paul.zhang,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'bi_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (panda,haya,jiangfeng,paul.zhang,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'fr_1.c':'filter=13045 AND created >= 2018-11-01 AND created <= 2018-12-31 AND component in (基础框架,数据源,swift,云端,x引擎,报表功能,填报,官方插件,计算引擎)',
    'fr_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2018-11-01 AND created <= 2018-12-31 AND 责任测试 in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo)',
    'fr_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo)',
    'fr_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo)',
    'sdet_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (april,kara,spruce,corleone,katherine,jiekai.bi,zhangyinga)',
    'sdet_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2018-11-01 AND created <= 2018-12-31 AND reporter in (april,kara,spruce,corleone,katherine,jiekai.bi,zhangyinga)'

}



judge_ab_201811_201812={
    "Abbie": {
        "3.f": "6"
  },
  "Abby": {
        "3.f": "42"
  },
  "Aloe": {
        "3.f": "42"
  },
  "Alisa": {
        "3.f": "42",
    '3.d':'91.8'
  },
  "Angle": {
        "3.f": "42"
  },
  "april": {
        "3.f": "2"
  },
  "Chanda": {
        "3.f": "66"
  },
  "Chaofan.Sun": {
        "3.f": "42"
  },
  "Chenyali": {
        "3.f": "8"
  },
  "connie": {
        "3.f": "42"
  },
  "Doris": {
        "3.f": "6"
  },
  "Fiona": {
        "3.f": "40"
  },
  "Gaojing": {
        "3.f": "6"
  },
  "Haiyang.Zhou": {
        "3.f": "42"
  },
  "haya": {
        "3.f": "6"
  },
  "jeo": {
        "3.f": "42",
    '3.d':'84.7'
  },
  "jiangfeng": {
        "3.f": "6"
  },
  "Kara": {
        "3.f": "4"
  },
  "Katherine": {
        "3.f": "2"
  },
  "katy": {
        "3.f": "4"
  },
  "Lena": {
        "3.f": "2"
  },
  "Lianbin.tu": {
        "3.f": "74"
  },
  "Lipei": {
        "3.f": "6",
    '3.d':'134.4'
  },
  "liucheng": {
        "3.f": "72"
  },
  "luna": {
        "3.f": "72"
  },
  "miley": {
        "3.f": "8"
  },
  "Min": {
        "3.f": "8"
  },
  "Neo.Zhu": {
        "3.f": "42",
    '3.d':'162.5'
  },
  "Niujialing": {
        "3.f": "6"
  },
  "Okcean": {
        "3.f": "42"
  },
  "panda": {
        "3.f": "6",
    '3.d':'118'
  },
  "Pandingling": {
        "3.f": "6"
  },
  "paul": {
        "3.f": "38",
    '3.d':'170.5'
  },
  "paul.zhang": {
        "3.f": "6"
  },
  "Qingzhi.Bao": {
        "3.f": "6"
  },
  "Sissi.Zhao": {
        "3.f": "8"
  },
  "spruce": {
        "3.f": "2"
  },
  "Syrena": {
        "3.f": "66"
  },
  "Wangshuyan": {
        "3.f": "6"
  },
  "Wuxinyu": {
        "3.f": "4"
  },
  "xiaoli.Jin": {
        "3.f": "72"
  },
  "Yina.Du": {
        "3.f": "48"
  },
  "zhaoxingpei": {
        "3.f": "8"
  },
  "Zoey": {
        "3.f": "42"
  }
}

single_ab_201901_201902={
    '1.a':'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 客户BUG AND created >= 2019-01-01 AND created <= 2019-02-28 AND NOT (问题解决方案 is not EMPTY AND 问题解决方案 in (不是bug, 需求处理, 文档优化, 永不修复, 产品改进) AND status in (创建者确认, 被否决)) AND NOT (问题解决方案 is not EMPTY AND 问题解决方案 in (重复BUG) AND status in (创建者验收, 创建者确认, 被否决, 已解决, 验收通过待发布, 产品场景确认)) AND (分支 = MASTER稳定版 OR 分支 is EMPTY) AND NOT status in (重复BUG待解决) AND 责任测试 = ',
    '1.b':'project in (BI, DEC, CHART, REPORT, MOBILE) AND issuetype = 开发测试任务 AND status in (创建者确认, 被否决) AND created >= 2019-01-01 AND created <= 2019-02-28 AND 研发退回原因 in (不是BUG) AND reporter = ',
    '1.f': '',
    '2.e': '',
    '3.a': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND (resolved >= 2019-01-01 AND resolved <= 2019-02-28) AND reporter = ',
    '3.b': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND (created >= 2019-01-01 AND created <= 2019-02-28) AND reporter = ',
    '1.g': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND reporter = ',
    '1.h':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND reporter = '

}
team_ab_201901_201902={
    'chart_1.c':'(filter = 13045 AND component in (报表图表, 扩展图表) OR filter = 13046 AND component in (BI图表, 图表)) AND created >= 2019-01-01 AND created <= 2019-02-28',
    'chart_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-01-01 AND created <= 2019-02-28 AND 责任测试 in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'chart_5.b': 'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'chart_5.c': 'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'dec_1.c':'filter=12925  AND created >= 2018-11-01 AND created <= 2018-12-31',
    'dec_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-01-01 AND created <= 2019-02-28 AND 责任测试 in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby)',
    'dec_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby)',
    'dec_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby)',
    'mobile_1.c':'filter=12924 AND created >= 2018-11-01 AND created <= 2018-12-31',
    'mobile_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-01-01 AND created <= 2019-02-28 AND 责任测试 in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,luna,lioucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'mobile_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,Chanda,luna,lioucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'mobile_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,Chanda,luna,lioucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'bi_1.c':'filter=13046 AND created >= 2019-01-01 AND created <= 2019-02-28 AND project != 决策平台 AND component in(X引擎,集群,性能,BI后端,BI前端)',
    'bi_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-01-01 AND created <= 2019-02-28 AND 责任测试 in (panda,haya,jiangfeng,paul.zhang,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'bi_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (panda,haya,jiangfeng,paul.zhang,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'bi_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (panda,haya,jiangfeng,paul.zhang,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'fr_1.c':'filter=13045 AND created >= 2019-01-01 AND created <= 2019-02-28 AND component in (基础框架,数据源,swift,云端,x引擎,报表功能,填报,官方插件,计算引擎)',
    'fr_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-01-01 AND created <= 2019-02-28 AND 责任测试 in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo)',
    'fr_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo)',
    'fr_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo)',
    'sdet_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (april,kara,spruce,corleone,katherine,jiekai.bi,zhangyinga)',
    'sdet_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-01-01 AND created <= 2019-02-28 AND reporter in (april,kara,spruce,corleone,katherine,jiekai.bi,zhangyinga)'

}
judge_ab_201901_201902={
}
single_ab_201903_201904={
    '1.a':'filter=16503 AND created >= 2019-03-01 AND created <= 2019-04-30 AND 责任测试 = ',
    '1.b':'project in (BI, DEC, CHART, REPORT, MOBILE) AND issuetype = 开发测试任务 AND status in (创建者确认, 被否决) AND created >= 2019-03-01 AND created <= 2019-04-30 AND 研发退回原因 in (不是BUG) AND reporter = ',
    '1.f': '',
    '2.e': '',
    '3.a': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND (resolved >= 2019-03-01 AND resolved <= 2019-04-30) AND reporter = ',
    '3.b': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND (created >= 2019-03-01 AND created <= 2019-04-30) AND reporter = ',
    '1.g': 'project in (报表, 决策平台, 图表开发, BI, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND reporter = ',
    '1.h':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND reporter = '

}
team_ab_201903_201904={
    'chart_1.c':'(filter = 13045 AND component in (报表图表, 扩展图表) OR filter = 13046 AND component in (BI图表, 图表)) AND created >= 2019-03-01 AND created <= 2019-04-30',
    'chart_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-03-01 AND created <= 2019-04-30 AND 责任测试 in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'chart_5.b': 'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND not (status in (创建者确认, 被否决) AND 研发退回原因 = 不是BUG) AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'chart_5.c': 'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (Lipei,Doris,Zoey,Alisa,Aloe,Amber,Tingting.Z,LuSun)',
    'dec_1.c':'filter=12925  AND created >= 2019-03-01 AND created <= 2019-04-30',
    'dec_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-03-01 AND created <= 2019-04-30 AND 责任测试 in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby)',
    'dec_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND not (status in (创建者确认, 被否决) AND 研发退回原因 = 不是BUG) AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby,BaoBao)',
    'dec_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (Yina.Du,Haiyang.Zhou,Neo.Zhu,Abby,BaoBao)',
    'mobile_1.c':'filter=12924 AND created >= 2018-11-01 AND created <= 2018-12-31',
    'mobile_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-03-01 AND created <= 2019-04-30 AND 责任测试 in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,luna,lioucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'mobile_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND not (status in (创建者确认, 被否决) AND 研发退回原因 = 不是BUG) AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,Chanda,luna,liucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'mobile_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (Miley,lianbin.tu,zhaoxingpei,Chenyali,Sissi.Zhao,"Min",Chanda,Chanda,luna,liucheng,xiaoli.Jin,Syrena,Cassie.wang)',
    'bi_1.c':'filter=13046 AND created >= 2019-03-01 AND created <= 2019-04-30 AND project != 决策平台 AND component in(X引擎,集群,性能,BI后端,BI前端)',
    'bi_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-03-01 AND created <= 2019-04-30 AND 责任测试 in (panda,haya,jiangfeng,paul.zhang,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'bi_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND not (status in (创建者确认, 被否决) AND 研发退回原因 = 不是BUG) AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (panda,haya,jiangfeng,paul.zhang,zhaoxingpei,Miley,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'bi_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (panda,haya,jiangfeng,paul.zhang,zhaoxingpei,Miley,qingzhi.bao,gaojing,abbie,pandingling,wangshuyan,katniss,yolanda,katy,wuxinyu,PearlNi)',
    'fr_1.c':'filter=13045 AND created >= 2019-03-01 AND created <= 2019-04-30 AND component in (基础框架,数据源,swift,云端,x引擎,报表功能,填报,官方插件,计算引擎)',
    'fr_3.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 客户BUG AND 问题解决方案 in (不是bug) AND status in (创建者确认, 被否决) AND created >= 2019-03-01 AND created <= 2019-04-30 AND 责任测试 in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo,Jerry.Qiao)',
    'fr_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND not (status in (创建者确认, 被否决) AND 研发退回原因 = 不是BUG) AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo,Jerry.Qiao)',
    'fr_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (fiona,paul,jeo,connie,angle,chaofan.sun,okcean,Taylor.mo,Jerry.Qiao)',
    'sdet_5.b':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND not (status in (创建者确认, 被否决) AND 研发退回原因 = 不是BUG) AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (april,kara,spruce,corleone,katherine,jiekai.bi,zhangyinga,Daniel.Feng)',
    'sdet_5.c':'project in (BI, REPORT, DEC, CHART, MOBILE) AND issuetype = 开发测试任务 AND status = 已解决 AND created >= 2019-03-01 AND created <= 2019-04-30 AND reporter in (april,kara,spruce,corleone,katherine,jiekai.bi,zhangyinga,Daniel.Feng)'

}
judge_ab_201903_201904={
}