# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class AutohomeItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 图片
    imgurl = scrapy.Field()
    # 简介
    neirong = scrapy.Field()
    # 详情链接
    xqurl = scrapy.Field()
    # 作者
    zuozhe = scrapy.Field()
    # 发布时间
    fbtime = scrapy.Field()
    # 全文
    alltext = scrapy.Field()
    # 浏览量(万)
    liulan = scrapy.Field()
    # 发布地点
    fbaddress = scrapy.Field()
    # 赞
    thumbsupnum = scrapy.Field()
    # 踩
    crazilynum = scrapy.Field()
    # 点击次数
    clicknum = scrapy.Field()
    # 收藏数
    storeupnum = scrapy.Field()
    # 评分
    totalscore = scrapy.Field()
    # 评论数
    discussnum = scrapy.Field()

