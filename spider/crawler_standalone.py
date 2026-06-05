#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
新能源资讯爬虫 + 数据生成器
爬取 autohome.com.cn 文章列表，自动生成点赞/收藏/评分等互动数据
"""

import os
import requests
from lxml import html
import pymysql
import random
import time
import re
import sys
from configparser import ConfigParser
from datetime import datetime

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_cfg = ConfigParser()
_cfg.read(os.path.join(_project_root, 'config.ini'), encoding='utf-8-sig')
DB_CONFIG = {
    'host': _cfg.get('sql', 'host'),
    'port': _cfg.getint('sql', 'port'),
    'user': _cfg.get('sql', 'user'),
    'password': _cfg.get('sql', 'passwd'),
    'database': _cfg.get('sql', 'db'),
    'charset': 'utf8mb4',
}

PAGES = 10           # 爬取页数
START_URL = 'https://www.autohome.com.cn/all/{}/#liststart'
DELAY = 1.0          # 请求间隔（秒）

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

# ============ DB ============
conn = pymysql.connect(**DB_CONFIG)
cursor = conn.cursor()

def insert_article(data):
    """插入文章数据"""
    cols = ', '.join(data.keys())
    qmarks = ', '.join(['%s'] * len(data))
    sql = f"INSERT INTO autohome ({cols}) VALUES ({qmarks})"
    try:
        cursor.execute(sql, tuple(data.values()))
        conn.commit()
        return True
    except Exception as e:
        print(f"  [INSERT ERROR] {e}")
        conn.rollback()
        return False

# ============ 爬虫逻辑 ============

def parse_list_page(page_num):
    """解析列表页，返回文章链接列表"""
    url = START_URL.format(page_num)
    print(f"\n[页面 {page_num}] 请求: {url}")

    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
    except Exception as e:
        print(f"  [ERROR] 请求失败: {e}")
        return []

    tree = html.fromstring(resp.text)
    items = tree.xpath('//ul[@class="article"]/li')
    print(f"  找到 {len(items)} 篇文章")

    articles = []
    for item in items:
        article = {}
        try:
            article['title'] = str(item.xpath('.//h3/text()')[0]).strip()
        except:
            article['title'] = ''
        try:
            article['imgurl'] = str(item.xpath('.//img/@src')[0]).strip()
        except:
            article['imgurl'] = ''
        try:
            article['neirong'] = str(item.xpath('.//p/text()')[0]).strip()
        except:
            article['neirong'] = ''
        try:
            article['xqurl'] = str(item.xpath('.//a/@href')[0]).strip()
        except:
            article['xqurl'] = ''

        articles.append(article)

    return articles


def parse_detail_page(article, hostname='www.autohome.com.cn', protocol='https'):
    """解析详情页，补充详细信息"""
    detail_url = article.get('xqurl', '')

    # 处理相对URL
    if not detail_url.startswith('http'):
        if detail_url.startswith('//'):
            detail_url = protocol + ':' + detail_url
        elif detail_url.startswith('/'):
            detail_url = protocol + '://' + hostname + detail_url
        else:
            detail_url = protocol + '://' + hostname + '/' + detail_url

    print(f"  详情: {detail_url[:80]}...")

    try:
        resp = requests.get(detail_url, headers=HEADERS, timeout=30)
    except Exception as e:
        print(f"    [ERROR] 请求失败: {e}")
        return article

    tree = html.fromstring(resp.text)

    # 作者
    try:
        article['zuozhe'] = str(tree.xpath('//span[contains(@class,"tw-line-clamp-1")]/text()')[0]).strip()
    except:
        article['zuozhe'] = ''

    # 发布时间
    try:
        article['fbtime'] = str(tree.xpath('//span[@class=" tw-ml-[4px]"]/text()')[0]).strip()
    except:
        article['fbtime'] = ''

    # 全文
    try:
        article['alltext'] = str(tree.xpath('string(//div[@id="parent-container"])')[0]).strip()
    except:
        article['alltext'] = ''

    # 浏览量（抓不到就生成随机值）
    try:
        liulan_text = tree.xpath('//span[comment() and contains(., "浏览")]/text()[1]')[0].strip()
        liulan_text = liulan_text.replace('万', '')
        article['liulan'] = int(float(liulan_text)) if '.' in liulan_text else int(liulan_text)
        if article['liulan'] == 0:
            article['liulan'] = random.randint(500, 50000)
    except:
        article['liulan'] = random.randint(500, 50000)

    # 发布地点
    try:
        article['fbaddress'] = str(tree.xpath('//span[@class=" tw-ml-[3px]"]/text()[2]')[0]).strip()
    except:
        article['fbaddress'] = ''

    return article


def generate_engagement():
    """生成随机互动数据"""
    return {
        'thumbsupnum': random.randint(0, 500),
        'crazilynum': random.randint(0, 30),
        'clicknum': random.randint(100, 10000),
        'storeupnum': random.randint(0, 100),
        'totalscore': round(random.uniform(3.0, 5.0), 1),
        'discussnum': random.randint(0, 50),
    }


# ============ 主程序 ============
if __name__ == '__main__':
    print("=" * 60)
    print("  新能源资讯爬虫 + 数据生成器")
    print(f"  目标: autohome 前 {PAGES} 页")
    print("=" * 60)

    total = 0
    inserted = 0

    for page in range(1, PAGES + 1):
        articles = parse_list_page(page)

        for article in articles:
            total += 1
            time.sleep(DELAY)

            # 爬详情
            article = parse_detail_page(article)

            # 生成互动数据
            engagement = generate_engagement()
            article.update(engagement)

            # 入库
            article.setdefault('title', '')
            article.setdefault('imgurl', '')
            article.setdefault('neirong', '')
            article.setdefault('xqurl', '')
            article.setdefault('zuozhe', '')
            article.setdefault('fbtime', '')
            article.setdefault('alltext', '')
            article.setdefault('liulan', 0)
            article.setdefault('fbaddress', '')
            article.setdefault('thumbsupnum', 0)
            article.setdefault('crazilynum', 0)
            article.setdefault('clicknum', 0)
            article.setdefault('storeupnum', 0)
            article.setdefault('totalscore', 0)
            article.setdefault('discussnum', 0)
            article['addtime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            print(f"    -> {article['title'][:40]} | 赞:{article['thumbsupnum']} 评:{article['totalscore']} 藏:{article['storeupnum']}")
            if insert_article(article):
                inserted += 1

    conn.close()

    print("\n" + "=" * 60)
    print(f"  完成！共 {total} 篇，成功入库 {inserted} 篇")
    print("=" * 60)
