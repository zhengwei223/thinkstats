"""解析twitter文本
每一行则是一个tweets（微博），里面有该微博的相关字段信息。

对应字段如下（每一个逗号分隔的，“”内的，则是字段的详细信息。空白则代表没有。）：

bid    消息ID
uid     用户ID
username 用户名
ugrade 用户等级字段
content(text) 微博内容
img(message包含图片链接)
created_at 微博发布时间
source(来源)
rt_num, 转发数
cm_num, 评论数
rt_uid, 转发UID
rt_username, 转发用户名
rt_v_class, 转发者等级
rt_content, 转发内容
rt_img, 转发内容所涉及图片
src_rt_num, 源微博回复数
src_cm_num, 源微博评论数
gender,(用户性别)
rt_mid（转发mid）
geo 地区
lat() 经度
lon 纬度
place 地点
hashtags
ats  @谁
rt_hashtags, 回复标签
rt_ats, 回复@谁
v_url, 源微博URL
rt_v_url 转发URL


twitter文本附件的排序格式如下

fields=bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url


而童鞋们，则需要利用自己已经掌握的知识，对其进行一个基本的文本分析。


注意：请用utf-8格式打开此文件。

要求如下：

1.该文本里，有多少个用户。（要求：输出为一个整数。）

2.该文本里，每一个用户的名字。 （要求：输出为一个list。）

3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）

4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）

5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）

6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）

7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets）

8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）

9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)

10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）

11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。

12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）

13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）

14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）

15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
"""
# coding=utf-8
import time

now = time.clock()
# 前期准备，整理数据
# 所有字段的名称放入元组
data_keys = (
    'bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid',
    'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location',
    'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links',
    'rt_hashtags',
    'rt_ats', 'v_url', 'rt_v_url')
# 记录字段名和其在行中出现位置的映射
keys = {data_keys[k]: k for k in range(0, len(data_keys))}

# 打开文件
fp = open("twitter.txt", "r", encoding='utf-8')
# 这其实是一个二维数组
lines = []


def init():
    # 解析文本每行为一个列表，将这些列表加入到field_table中，这样就有了一个二维表
    for i, line in enumerate(fp):
        list_by_line = line[1:-1].split('","')
        lines.append(list_by_line)


# print(lines[1])

# 1 输出用户总数

def e1():
    res = len(set([line[keys['uid']] for line in lines]))
    return res


# 2 每一个用户的名字 list
def e2():
    users = set([line[keys['username']] for line in lines])
    return (len(users), users)


# 3 有多少个2012年11月发布的tweets
def e3(ym='2012-11'):
    res = len(list(filter(lambda line: line[keys['created_at']].startswith(ym), lines)))
    return res


# 4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
def e4():
    return (list(set([line[keys['created_at']][0:10] for line in lines])))


# 5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）
def e5():
    hours_list = [int(line[keys['created_at']][11:13]) for line in lines]
    hour_count_tup_list = [(h, hours_list.count(h)) for h in range(0, 24)]
    hour_count_tup_list.sort(key=lambda x: x[1], reverse=True)
    return hour_count_tup_list


# 6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）
def e6():
    day_list = e4()  # 所有日期
    day_userAndCount_map = {day: dict() for day in day_list}
    # print(day_userAndCount_map)
    for line in lines:
        day = line[keys['created_at']][0: 10]  # 日期
        _username = line[keys['username']]  # username
        if _username in day_userAndCount_map[day]:
            day_userAndCount_map[day][_username] += 1
        else:
            day_userAndCount_map[day][_username] = 1
    day_max_map = {}
    for day, user_count in day_userAndCount_map.items():
        username = sorted(user_count.items(), key=lambda x: x[1], reverse=True)[0]
        day_max_map[day] = username
    return day_max_map


# 7 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率
def e7(day='2012-11-03'):
    hour_list_in_that_day = [int(line[keys['created_at']][11:13]) for line in lines if
                             line[keys['created_at']][0:10] == day]
    return [(h, hour_list_in_that_day.count(h)) for h in range(0, 24)]
    # print(hour_list_in_that_day)


# 8 统计该文本里，来源的相关信息和次数

def e8():
    source_count_map = {}
    for line in lines:
        source = line[keys['source']]
        if source in source_count_map:
            source_count_map[source] += 1
        else:
            source_count_map[source] = 1
    return source_count_map


# 9 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个

def e9():
    uml_total = 0
    for line in lines:
        if line[keys['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta'):
            uml_total += 1

    return uml_total


# 10 UID为573638104的用户 发了多少个微博
def e10(uid):
    tweet_total_by_user = 0
    for line in lines:
        if line[keys['uid']] == uid:
            tweet_total_by_user += 1

    return tweet_total_by_user


# 11 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微博数最多的用户uid。

def e11(*uid):
    uid_max = ''
    count_max = 0
    for id in uid:
        _count = e10(id)
        if _count > count_max:
            count_max = _count
            uid_max = id
    return (uid_max, count_max)


# 12 该文本里，谁发的微博内容长度最长
def e12():
    sorted_list = [(line[keys['username']], len(line[keys['content']]), line[keys['content']]) for line in lines]
    sorted_list.sort(key=lambda x: x[1],
                     reverse=True)
    return sorted_list[0]


# 13 该文本里，谁转发的URL最多
def e13():
    id_rtnum = [(line[keys['uid']], line[keys['rt_num']]) for line in lines if line[keys['rt_num']] != '']
    id_rtnum.sort(key=lambda x: x[1], reverse=True)
    return id_rtnum[0]


# 14 该文本里，11点钟，谁发的微博次数最多。
def e14():
    usernames_11_clock = [line[keys['username']] for line in lines if int(line[keys['created_at']][11: 13]) == 11]
    username_count_tup_list = [(username, usernames_11_clock.count(username)) for username in set(usernames_11_clock)]
    username_count_tup_list.sort(key=lambda x: x[1], reverse=True)
    return username_count_tup_list[0]


# 15. 该文本里，哪个用户的源微博URL(v_url)次数最多。 （要求：输出用户的uid，字符串格式。）
def e15():
    uids_by_vurl = [line[keys['uid']] for line in lines if line[keys['v_url']] != '']  # v_url有效的微博条目中的userid放入一个列表
    uid_count_tup_list = [(uid, uids_by_vurl.count(uid)) for uid in set(uids_by_vurl)]
    uid_count_tup_list.sort(key=lambda x: x[1], reverse=True)
    return uid_count_tup_list[0]


init()
print("该文本中总共出现了{}个用户id".format(e1()))
print("用户的名字", e2()[1])
print("2012年11月发布的tweets数目是{}".format(e3()))
print("文本中有微博记录的日期是", e4())
print("统计每个小时微博的总数，逆序排列", e5())
print("每一天发表tweets最多的用户及其发表量", e6())
print("'2012-11-03'每个小时微博数的统计", e7())
print("来源统计：", e8())
print('以https://twitter.com/umiushi_no_uta开头的url条数', e9())
print('573638104总共发了%d条微博' % e10('573638104'))
print("这些人中发微博数量最多的是{0},他发了{1}条".format(*e11('28803555', '573638104', '72047320')))
print("发送内容长度最长的是", e12())
print("{0}发url最多,次数为{0}".format(*e13()))
print("11点__{0}__发微博最多,条数为{0}".format(*e14()))
print("源微博地址最多的是__{0}__，数目为：{0}".format(*e15()))
print('运算时间：%s' % (time.clock() - now))  # 整体运行时间)

# # 现在把每天发布最多的那个人找出来
# dateAndMax = {}
# for day, userAndCount in dateAndStats.items():
#     dateAndMax[day] = sorted(userAndCount.items(), key=lambda x: x[1], reverse=True)[0][0]
#
# print("按每天统计发布微博数量最多的人：", dateAndMax)
#
#
# def hourAndCountInDay(y, m, d):
#     res = {}
#     for _record in field_table:
#         try:
#             time_struct = time.strptime(_record[6], '%Y-%m-%d %H:%M:%S')
#             if time_struct.tm_year == y and time_struct.tm_mon == m and time_struct.tm_mday == d:
#                 if time_struct.tm_hour not in res:
#                     res[time_struct.tm_hour] = 0
#                 res[time_struct.tm_hour] += 1
#
#         except ValueError:
#             continue
#
#     return res
#
#
# print("2012-11-3按小时统计发布量", hourAndCountInDay(2012, 11, 3).items())
fp.close()
