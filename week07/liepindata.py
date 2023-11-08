

city = [{'code': '410', 'name': '全国'},
 {'code': '010', 'name': '北京'},
 {'code': '020', 'name': '上海'},
 {'code': '030', 'name': '天津'},
 {'code': '040', 'name': '重庆'},
 {'code': '050020', 'name': '广州'},
 {'code': '050090', 'name': '深圳'},
 {'code': '060080', 'name': '苏州'},
 {'code': '060020', 'name': '南京'},
 {'code': '070020', 'name': '杭州'},
 {'code': '210040', 'name': '大连'},
 {'code': '280020', 'name': '成都'},
 {'code': '170020', 'name': '武汉'},
 {'code': '270020', 'name': '西安'}]

workExperiences = [{'code': '1', 'name': '应届生'},
 {'code': '2', 'name': '实习生'},
 {'code': '0$1', 'name': '1年以内'},
 {'code': '1$3', 'name': '1-3年'},
 {'code': '3$5', 'name': '3-5年'},
 {'code': '5$10', 'name': '5-10年'},
 {'code': '10$999', 'name': '10年以上'}]

# header准备
def headers():
    liepin_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "487",
        "Content-Type": "application/json;charset=UTF-8;",
        "Cookie": "XSRF-TOKEN=zIARnRM0QQaLudJk_4OBXw; __gc_id=e936feed5bd343e5a73b304fa0d4ad5f; _ga=GA1.1.504776059.1697021947; __uuid=1697021948310.51; __tlog=1697021948354.48%7C00000000%7C00000000%7C00000000%7C00000000; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1697021951; acw_tc=2760828416970219810274366e53a098388abcfc886c89f5cbf2332344893f; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1697021975; __session_seq=4; __uv_seq=4; __tlg_event_seq=24; _ga_54YTJKWN86=GS1.1.1697021946.1.1.1697023027.0.0.0",
        "Host": "api-c.liepin.com",
        "Origin": "https://www.liepin.com",
        "Referer": "https://www.liepin.com/zhaopin/?currentPage=0&pageSize=40&city=050090&dq=050090&pubTime=&key=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&suggestTag=&otherCity=&industry=&ckId=geq5b0qsi9umzbhn0oojbi2j8v8qu2bb&scene=condition&skId=geq5b0qsi9umzbhn0oojbi2j8v8qu2bb&fkId=geq5b0qsi9umzbhn0oojbi2j8v8qu2bb&sfrom=search_job_pc&suggestId=",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
        "X-Client-Type": "web",
        "X-Fscp-Bi-Stat": "{\"location\": \"https://www.liepin.com/zhaopin/?currentPage=0&pageSize=40&city=050090&dq=050090&pubTime=&key=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&suggestTag=&otherCity=&industry=&ckId=geq5b0qsi9umzbhn0oojbi2j8v8qu2bb&scene=condition&skId=geq5b0qsi9umzbhn0oojbi2j8v8qu2bb&fkId=geq5b0qsi9umzbhn0oojbi2j8v8qu2bb&sfrom=search_job_pc&suggestId=\"}",
        "X-Fscp-Fe-Version": "",
        "X-Fscp-Std-Info": "{\"client_id\": \"40108\"}",
        "X-Fscp-Trace-Id": "187c89d1-ed19-48b2-99fe-85ceeb116589",
        "X-Fscp-Version": "1.1",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "zIARnRM0QQaLudJk_4OBXw"
    }

    return liepin_headers


# 准备城市code
def choose_city(city_name):
    for i in city:
        if i['name'] == city_name:
            return i['code']

# 准备工作经验code
def choose_WE(工作经验):
    for i in workExperiences:
        if i['name'] == 工作经验:
            return i['code']
# 准备payload
def request_payload(城市,关键词,工作经验):
    payload = {
        "data": {
            "mainSearchPcConditionForm": {
                "city": choose_city(城市),
                "dq": choose_city(城市),
                "pubTime": "",
                "currentPage": "0",
                "pageSize": 40,
                "key": 关键词,
                "suggestTag": "",
                "workYearCode": choose_WE(工作经验),
                "compId": "",
                "compName": "",
                "compTag": "",
                "industry": "",
                "salary": "",
                "jobKind": "",
                "compScale": "",
                "compKind": "",
                "compStage": "",
                "eduLevel": ""
            },
            "passThroughForm": {
                "scene": "condition",
                "skId": "geq5b0qsi9umzbhn0oojbi2j8v8qu2bb",
                "fkId": "geq5b0qsi9umzbhn0oojbi2j8v8qu2bb",
                "ckId": "y2jy1uvl2gar8xipyemg77rijoomop78",
                "suggest": None
            }
        }
    }
    return payload
    