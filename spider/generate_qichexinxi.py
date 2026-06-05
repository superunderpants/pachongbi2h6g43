#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
汽车信息数据生成器
写死 30 款热门新能源车型，含事故率、价格、销量等参数
"""
import os
import pymysql
import random
from configparser import ConfigParser
from datetime import datetime, timedelta

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

PICTURE_POOL = [
    'https://www2.autoimg.cn/chejiahaodfs/g34/M01/73/67/400x300_0_autohomecar__ChtpWGof7bGAO3O8ABF6kaUkXaE274.png',
    'https://www2.autoimg.cn/chejiahaodfs/g34/M08/76/4E/400x300_0_autohomecar__ChxpWGof99WATTGvAAIGiQiH5Ew28.jpeg',
    'https://www2.autoimg.cn/chejiahaodfs/g33/M02/79/84/400x300_0_autohomecar__ChxpVmof9keAKshyAA6F_xvzuZI123.png',
    'https://www2.autoimg.cn/chejiahaodfs/g33/M0B/78/F7/400x300_0_autohomecar__Chto52of6tyARaN7AAjI-BpXrwA270.png',
    'https://www2.autoimg.cn/chejiahaodfs/g33/M02/79/1E/400x300_0_autohomecar__ChxpVWof7tWAJsKAABLcdrLAMxM438.png',
    'https://www2.autoimg.cn/chejiahaodfs/g34/M07/75/C0/400x300_0_autohomecar__ChxpWGof7Y-ABf-pAAzAHr3jmrE797.png',
    'https://img3.autoimg.cn/chejiahaodfs/g33/M02/78/33/400x300_0_autohomecar__ChxpVWof4AeALFRyAAaTJjYDIWo603.jpg',
    'https://www2.autoimg.cn/chejiahaodfs/g33/M01/77/F1/400x300_0_autohomecar__ChxpVWof25GANDhuABeQB6YW_FQ029.png',
]

CARS = [
    {
        'chepinpai': '比亚迪',
        'chexinghao': '海豹06 DM-i',
        'jiage': '9.98-13.98万',
        'xiaoliang': 28500,
        'shigulv': 1.8,
        'xuhang': 2100,
        'dianchileixing': '磷酸铁锂刀片电池',
        'cheshenleixing': '轿车',
        'shangshishijian': '2025-03-15',
        'jianjie': '比亚迪海洋网全新中型轿车，搭载第五代DM混动技术，综合续航突破2100公里，以不到10万的起售价树立了混动市场新标杆。',
        'canshu': '【基本参数】\n车身尺寸：4830×1875×1495mm | 轴距：2790mm\n发动机：1.5L 74kW 阿特金森循环\n电动机：120kW 永磁同步\n系统综合功率：173kW\n0-100km/h加速：7.3秒\nWLTC综合油耗：1.08L/100km\n纯电续航：121km（CLTC）\n综合续航：2100km（CLTC）\n\n【底盘与安全】\n前麦弗逊+后多连杆独立悬架\nESP车身稳定系统 | 8安全气囊\nL2级DiPilot智能驾驶辅助\n\n【智能配置】\n12.8英寸自适应旋转悬浮Pad\nDiLink 5.0智能网联系统\n手机NFC车钥匙 | 50W无线快充',
    },
    {
        'chepinpai': '比亚迪',
        'chexinghao': '宋PLUS DM-i',
        'jiage': '13.58-17.58万',
        'xiaoliang': 35200,
        'shigulv': 1.5,
        'xuhang': 1250,
        'dianchileixing': '磷酸铁锂刀片电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-11-20',
        'jianjie': '比亚迪王朝网销量担当，插混SUV市场标杆，累计销量突破150万辆，以可靠品质和均衡产品力持续领跑细分市场。',
        'canshu': '【基本参数】\n车身尺寸：4775×1890×1670mm | 轴距：2765mm\n发动机：1.5L 81kW\n电动机：145kW\n系统综合功率：213kW\n0-100km/h加速：7.9秒\n纯电续航：150km（CLTC）\n综合续航：1250km（CLTC）\n\n【配置亮点】\n15.6英寸自适应旋转屏\nDiPilot智能驾驶辅助\nV2L车外放电 | 手机远程控制',
    },
    {
        'chepinpai': '比亚迪',
        'chexinghao': '元PLUS',
        'jiage': '11.98-14.98万',
        'xiaoliang': 31800,
        'shigulv': 1.2,
        'xuhang': 510,
        'dianchileixing': '磷酸铁锂刀片电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-09-10',
        'jianjie': 'e平台3.0首款A级SUV，全球累计销量超80万辆，出口至50+国家，以三电技术领先和高性价比获得全球市场认可。',
        'canshu': '【基本参数】\n车身尺寸：4455×1875×1615mm | 轴距：2720mm\n电机功率：150kW\n0-100km/h加速：7.3秒\n电池容量：49.92/60.48kWh\n续航：430/510km（CLTC）\n\n【底盘与充电】\n前麦弗逊+后多连杆独立悬架\n快充30%-80%：30分钟\n支持最高85kW直流快充\n\n【智能配置】\n12.8英寸自适应旋转屏\nOTA远程升级 | 手机NFC钥匙',
    },
    {
        'chepinpai': '比亚迪',
        'chexinghao': '汉EV 冠军版',
        'jiage': '18.98-28.98万',
        'xiaoliang': 16800,
        'shigulv': 1.6,
        'xuhang': 715,
        'dianchileixing': '磷酸铁锂刀片电池',
        'cheshenleixing': '轿车',
        'shangshishijian': '2024-08-05',
        'jianjie': '比亚迪旗舰纯电轿车，累计销量超60万辆，刀片电池+CTB技术+云辇-C智能车身控制，定义中国品牌中大型轿车新高度。',
        'canshu': '【基本参数】\n车身尺寸：4995×1910×1495mm | 轴距：2920mm\n电机功率：180/380kW（四驱）\n0-100km/h加速：3.9秒（四驱版）\n电池容量：85.4kWh\n续航：715km（CLTC单电机）/ 610km（四驱）\n\n【底盘与智能】\n云辇-C智能阻尼车身控制\n前双叉臂+后五连杆独立悬架\nDiPilot 300智能驾驶辅助\n800V高压快充平台',
    },
    {
        'chepinpai': '特斯拉',
        'chexinghao': 'Model Y',
        'jiage': '24.99-35.49万',
        'xiaoliang': 48200,
        'shigulv': 2.1,
        'xuhang': 688,
        'dianchileixing': '三元锂/磷酸铁锂',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-10-15',
        'jianjie': '全球最畅销电动SUV，2024年全球销量超120万辆，以极简设计、领先能效和超级充电网络持续领跑全球电动车市场。',
        'canshu': '【基本参数】\n车身尺寸：4750×1921×1624mm | 轴距：2890mm\n电机功率：220/331/357kW\n0-100km/h加速：5.9/5.0/3.7秒（后驱/长续航/性能版）\n电池容量：60/78.4kWh\n续航：554/688/615km（CLTC）\n\n【智能配置】\n15英寸中控触屏 | 标配Autopilot\n可选FSD全自动驾驶（买断6.4万）\nOTA空中升级 | 哨兵模式\n\n【充电网络】\n全国超2000座超级充电站\nV3超充：15分钟补充250km',
    },
    {
        'chepinpai': '特斯拉',
        'chexinghao': 'Model 3',
        'jiage': '23.19-33.19万',
        'xiaoliang': 22100,
        'shigulv': 2.3,
        'xuhang': 606,
        'dianchileixing': '磷酸铁锂/三元锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2024-09-20',
        'jianjie': '特斯拉入门轿车标杆，焕新版在外观、内饰、舒适性上全面升级，风阻系数仅0.219Cd，以极致能效和品牌魅力吸引年轻用户。',
        'canshu': '【基本参数】\n车身尺寸：4720×1848×1442mm | 轴距：2875mm\n风阻系数：0.219Cd\n0-100km/h加速：6.1/4.4秒（后驱/长续航）\n电池容量：60/78.4kWh\n续航：606/713km（CLTC）\n\n【焕新升级】\n全新前后灯组设计 | 双层隔音玻璃\n前排座椅通风 | 后排8英寸控制屏\n256色氛围灯 | 17扬声器音响',
    },
    {
        'chepinpai': '理想',
        'chexinghao': 'L6',
        'jiage': '24.98-29.98万',
        'xiaoliang': 38500,
        'shigulv': 1.4,
        'xuhang': 1390,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2025-04-10',
        'jianjie': '理想品牌最畅销车型，上市首月订单破4万辆，六座家庭SUV，增程式动力+冰箱彩电大沙发，精准满足家庭出行需求。',
        'canshu': '【基本参数】\n车身尺寸：4925×1960×1735mm | 轴距：2920mm\n增程器：1.5T 四缸 113kW\n系统综合功率：330kW\n0-100km/h加速：5.3秒\n纯电续航：212km（CLTC）\n综合续航：1390km（CLTC）\n\n【家庭配置】\n六座布局（2+2+2）\n13.35英寸HUD | 15.7英寸中控屏\nAD Max智能驾驶（激光雷达+双目视觉）\n三区独立空调 | 后排冷暖冰箱',
    },
    {
        'chepinpai': '理想',
        'chexinghao': 'L7',
        'jiage': '30.98-37.98万',
        'xiaoliang': 15200,
        'shigulv': 1.3,
        'xuhang': 1315,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-07-15',
        'jianjie': '理想L系列五座旗舰，大五座布局提供更宽适的二排空间，空气悬架+CDC减震器打造越级的乘坐舒适性。',
        'canshu': '【基本参数】\n车身尺寸：5050×1995×1750mm | 轴距：3005mm\n增程器：1.5T 四缸 113kW\n系统综合功率：330kW\n0-100km/h加速：5.3秒\n纯电续航：210km（CLTC）\n综合续航：1315km（CLTC）\n\n【豪华配置】\n空气悬架+CDC连续可变阻尼\n21扬声器杜比全景声音响\n后排座椅按摩 | 静音电吸门\n智能驾驶AD Max',
    },
    {
        'chepinpai': '蔚来',
        'chexinghao': 'ET5',
        'jiage': '29.80-35.60万',
        'xiaoliang': 8500,
        'shigulv': 1.7,
        'xuhang': 710,
        'dianchileixing': '三元锂/磷酸铁锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2024-11-08',
        'jianjie': '蔚来NT2.0平台中型轿跑，4.3秒破百、换电仅需3分钟，以换电模式和高品质服务构建差异化竞争力。',
        'canshu': '【基本参数】\n车身尺寸：4790×1960×1499mm | 轴距：2888mm\n电机功率：360kW（前后双电机）\n0-100km/h加速：4.3秒\n电池容量：75/100kWh\n续航：560/710km（CLTC）\n\n【智能配置】\nNIO Aquila超感系统（33传感器）\nNAD自动驾驶（激光雷达+4xOrin）\nPanoCinema全景数字座舱\n\n【换电服务】\n全国2400+换电站\n3分钟快速换电 | BaaS电池租赁',
    },
    {
        'chepinpai': '蔚来',
        'chexinghao': 'ES6',
        'jiage': '33.80-39.60万',
        'xiaoliang': 9800,
        'shigulv': 1.5,
        'xuhang': 625,
        'dianchileixing': '三元锂/磷酸铁锂',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-06-20',
        'jianjie': '蔚来销量主力中型SUV，NT2.0平台全栈自研，兼具4.5秒加速性能与豪华舒适，是蔚来换电模式的最佳载体之一。',
        'canshu': '【基本参数】\n车身尺寸：4854×1995×1703mm | 轴距：2915mm\n电机功率：360kW（前后双电机）\n0-100km/h加速：4.5秒\n电池容量：75/100kWh\n续航：490/625km（CLTC）\n\n【舒适配置】\n空气悬架+CDC动态悬架阻尼控制\n杜比全景声7.1.4沉浸式音响\n女王副驾 | 前排座椅通风加热按摩',
    },
    {
        'chepinpai': '小鹏',
        'chexinghao': 'MONA M03',
        'jiage': '12.98-17.98万',
        'xiaoliang': 18500,
        'shigulv': 1.9,
        'xuhang': 620,
        'dianchileixing': '磷酸铁锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2025-05-08',
        'jianjie': '小鹏MONA系列首款车型，定位年轻化智能轿跑，12.98万起标配XNGP全场景智驾，以"智驾平权"打开15万级市场。',
        'canshu': '【基本参数】\n车身尺寸：4780×1896×1445mm | 轴距：2765mm\n风阻系数：0.194Cd（全球量产车最低）\n电机功率：160kW\n0-100km/h加速：6.9秒\n电池容量：51.8/62.2kWh\n续航：515/620km（CLTC）\n\n【智驾核心】\nXNGP全场景智能辅助驾驶（纯视觉）\n高速NGP+城市NGP+记忆泊车\n12个摄像头+12个超声波雷达',
    },
    {
        'chepinpai': '小鹏',
        'chexinghao': 'G6',
        'jiage': '19.99-27.69万',
        'xiaoliang': 10500,
        'shigulv': 1.8,
        'xuhang': 755,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-08-25',
        'jianjie': '小鹏SEPA2.0平台首款车型，800V高压快充+755km超长续航，以技术和智驾见长的纯电中型SUV。',
        'canshu': '【基本参数】\n车身尺寸：4753×1920×1650mm | 轴距：2890mm\n电机功率：218/358kW（后驱/四驱）\n0-100km/h加速：6.2/3.9秒\n电池容量：66/87.5kWh\n续航：580/755km（CLTC）\n\n【800V快充】\n充电5分钟续航200km\n10%-80%快充仅需20分钟',
    },
    {
        'chepinpai': '极氪',
        'chexinghao': '007',
        'jiage': '17.99-28.99万',
        'xiaoliang': 12800,
        'shigulv': 1.6,
        'xuhang': 870,
        'dianchileixing': '磷酸铁锂/三元锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2025-03-28',
        'jianjie': '极氪品牌纯电轿车，全系800V高压平台+最高500kW超快充，充电15分钟续航500km，续航最高870km。',
        'canshu': '【基本参数】\n车身尺寸：4865×1900×1450mm | 轴距：2928mm\n电机功率：310/475kW（后驱/四驱）\n0-100km/h加速：5.4/2.84秒\n电池容量：75/100kWh\n续航：616/870km（CLTC）\n\n【超快充】\n全系800V高压平台\n最高500kW超快充\n充电15分钟续航500km+',
    },
    {
        'chepinpai': '极氪',
        'chexinghao': '001',
        'jiage': '26.90-34.90万',
        'xiaoliang': 9200,
        'shigulv': 2.0,
        'xuhang': 741,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': '猎装轿跑',
        'shangshishijian': '2024-10-08',
        'jianjie': '极氪首款车型，猎装轿跑定位独树一帜，3.8秒破百+741km续航，以差异化设计和出色性能获得忠实用户群体。',
        'canshu': '【基本参数】\n车身尺寸：4970×1999×1560mm | 轴距：3005mm\n电机功率：310/580kW（后驱/四驱）\n0-100km/h加速：5.9/3.8秒\n电池容量：100kWh\n续航：741/656km（CLTC）\n\n【特色配置】\n猎装轿跑造型 | 电动尾翼\n22英寸锻造轮毂 | Brembo六活塞卡钳\n22扬声器雅马哈音响',
    },
    {
        'chepinpai': '问界',
        'chexinghao': 'M7',
        'jiage': '24.98-32.98万',
        'xiaoliang': 21200,
        'shigulv': 1.3,
        'xuhang': 1300,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-12-15',
        'jianjie': '华为鸿蒙智行旗下热销增程SUV，搭载华为ADS 2.0高阶智驾，智能座舱+鸿蒙生态联动是核心竞争力。',
        'canshu': '【基本参数】\n车身尺寸：5020×1945×1760mm | 轴距：2820mm\n增程器：1.5T 四缸 112kW\n系统综合功率：330kW\n0-100km/h加速：5.0秒\n纯电续航：240km（CLTC）\n综合续航：1300km（CLTC）\n\n【华为技术】\n华为ADS 2.0高阶智驾\n鸿蒙智能座舱（HarmonyOS）\nHUAWEI SOUND音响\n超级桌面（手机应用无缝上车）',
    },
    {
        'chepinpai': '问界',
        'chexinghao': 'M9',
        'jiage': '46.98-56.98万',
        'xiaoliang': 11500,
        'shigulv': 1.1,
        'xuhang': 1400,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2025-01-20',
        'jianjie': '问界品牌旗舰大型SUV，华为全栈技术加持，激光雷达+ADS 3.0+鸿蒙座舱，50万级新能源SUV销量榜首。',
        'canshu': '【基本参数】\n车身尺寸：5230×1999×1800mm | 轴距：3110mm\n增程器：1.5T 四缸 112kW\n系统综合功率：390kW\n0-100km/h加速：4.9秒\n纯电续航：275km（CLTC）\n综合续航：1400km（CLTC）\n\n【旗舰配置】\n华为ADS 3.0（192线激光雷达）\n后排零重力座椅+投影幕布\n双50W无线快充 | 冷暖冰箱\n25扬声器HUAWEI SOUND卓越系列',
    },
    {
        'chepinpai': '小米',
        'chexinghao': 'SU7',
        'jiage': '21.59-29.99万',
        'xiaoliang': 19500,
        'shigulv': 2.2,
        'xuhang': 830,
        'dianchileixing': '磷酸铁锂/三元锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2025-02-28',
        'jianjie': '小米汽车首款量产车型，以极致性能和生态联动打开市场，上市即爆款，重新定义20万级纯电轿车产品标准。',
        'canshu': '【基本参数】\n车身尺寸：4997×1963×1455mm | 轴距：3000mm\n风阻系数：0.195Cd\n电机功率：220/495kW（后驱/双电机）\n0-100km/h加速：5.28/2.78秒\n电池容量：73.6/101kWh\n续航：668/830km（CLTC）\n\n【生态联动】\n澎湃OS车机系统 | 小米手机无缝流转\nCarIoT车载生态（扩展接口）\n支持CarPlay/Android Auto\n56英寸HUD+翻转仪表屏',
    },
    {
        'chepinpai': '长安',
        'chexinghao': '深蓝SL03',
        'jiage': '14.59-19.19万',
        'xiaoliang': 11500,
        'shigulv': 2.5,
        'xuhang': 705,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': '轿车',
        'shangshishijian': '2024-09-28',
        'jianjie': '长安深蓝品牌首款车型，提供纯电/增程/氢电三种动力，时尚运动设计+后驱布局吸引年轻消费者。',
        'canshu': '【基本参数】\n车身尺寸：4820×1890×1480mm | 轴距：2900mm\n电机功率：160/190kW\n0-100km/h加速：6.9/5.9秒\n电池容量：58/79.97kWh\n续航：515/705km（CLTC）\n增程版综合续航：1200km\n\n【配置亮点】\n后驱布局 | 无框车门+隐藏式门把手\n14.6英寸向日葵屏（左右各15°旋转）\n高通8155芯片',
    },
    {
        'chepinpai': '长安',
        'chexinghao': '启源A07',
        'jiage': '11.99-15.99万',
        'xiaoliang': 14200,
        'shigulv': 1.9,
        'xuhang': 710,
        'dianchileixing': '磷酸铁锂/三元锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2025-04-18',
        'jianjie': '长安启源A07"真香版"，11.99万起的中型轿车，高通8155芯片+15.6英寸中控屏+AR-HUD，超高性价比之选。',
        'canshu': '【基本参数】\n车身尺寸：4905×1910×1480mm | 轴距：2900mm\n电机功率：160kW\n电池容量：58.1/79.97kWh\n续航：515/710km（CLTC）\n增程版综合续航：1200km\n\n【配置核心】\n高通骁龙8155芯片\n15.6英寸中控屏+AR-HUD\n50W手机无线充电\n前排座椅通风加热按摩',
    },
    {
        'chepinpai': '吉利',
        'chexinghao': '银河E8',
        'jiage': '17.58-22.88万',
        'xiaoliang': 9200,
        'shigulv': 1.7,
        'xuhang': 665,
        'dianchileixing': '磷酸铁锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2024-11-25',
        'jianjie': '吉利银河系列旗舰纯电轿车，45英寸8K贯穿大屏+8295芯片+800V快充，以越级配置冲击20万级轿车市场。',
        'canshu': '【基本参数】\n车身尺寸：5010×1920×1465mm | 轴距：2925mm\n电机功率：200/475kW（后驱/四驱）\n0-100km/h加速：5.4/3.5秒\n电池容量：62/76kWh\n续航：550/665km（CLTC）\n\n【越级配置】\n45英寸8K无界智慧霸屏\n高通8295芯片 | Flyme Auto车机\n800V超快充 | 25.6英寸AR-HUD',
    },
    {
        'chepinpai': '五菱',
        'chexinghao': '星光纯电版',
        'jiage': '7.98-9.98万',
        'xiaoliang': 25800,
        'shigulv': 2.8,
        'xuhang': 410,
        'dianchileixing': '磷酸铁锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2025-05-20',
        'jianjie': '五菱星光纯电版，7.98万起入门价搅动A0级纯电市场，410km续航满足日常通勤，"人民的代步车"再进化。',
        'canshu': '【基本参数】\n车身尺寸：4380×1750×1505mm | 轴距：2600mm\n电机功率：70kW\n电池容量：42kWh\n续航：410km（CLTC）\n快充30%-80%：约30分钟\n\n【配置亮点】\n10.25英寸中控触屏\n倒车影像+后雷达\n手机互联映射\n电子驻车+自动空调',
    },
    {
        'chepinpai': '五菱',
        'chexinghao': '缤果PLUS',
        'jiage': '5.98-8.48万',
        'xiaoliang': 32500,
        'shigulv': 3.1,
        'xuhang': 333,
        'dianchileixing': '磷酸铁锂',
        'cheshenleixing': '微型车',
        'shangshishijian': '2024-12-28',
        'jianjie': '五菱缤果PLUS，5.98万起售的微型纯电车，月销超3万辆，以极致性价比成为城市代步首选。',
        'canshu': '【基本参数】\n车身尺寸：3950×1708×1580mm | 轴距：2560mm\n电机功率：30/50kW\n电池容量：17.3/31.0kWh\n续航：203/333km（CLTC）\n\n【城市代步】\n超小转弯半径4.3米\n支持家用220V充电\n手机App远程控制空调\n后排可放倒扩展储物空间',
    },
    {
        'chepinpai': '长城',
        'chexinghao': '坦克700 Hi4-T',
        'jiage': '40.00-50.00万',
        'xiaoliang': 3800,
        'shigulv': 1.0,
        'xuhang': 900,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': '硬派越野SUV',
        'shangshishijian': '2025-04-25',
        'jianjie': '坦克品牌旗舰硬派越野SUV，3.0T V6+Hi4-T混动+三把锁+空气悬架，中国品牌硬派越野新高度。',
        'canshu': '【基本参数】\n车身尺寸：5090×2061×1952mm | 轴距：3000mm\n发动机：3.0T V6 双涡轮 260kW\n系统综合功率：385kW | 综合扭矩：850Nm\n0-100km/h加速：5.8秒\n纯电续航：120km\n\n【越野装备】\n智能四驱+三把差速锁（前/中/后）\n坦克转弯+蠕行模式\n自适应空气悬架（可调120mm）\n涉水深度900mm',
    },
    {
        'chepinpai': '广汽埃安',
        'chexinghao': 'AION Y Plus',
        'jiage': '9.98-15.98万',
        'xiaoliang': 23800,
        'shigulv': 2.2,
        'xuhang': 610,
        'dianchileixing': '磷酸铁锂',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-10-30',
        'jianjie': '埃安品牌最畅销车型之一，大空间纯电SUV，610km续航+弹匣电池安全性，在网约车和家用市场均有强势表现。',
        'canshu': '【基本参数】\n车身尺寸：4535×1870×1650mm | 轴距：2750mm\n电机功率：150kW\n电池容量：63.98/76.8kWh\n续航：510/610km（CLTC）\n\n【空间与安全】\n弹匣电池技术（针刺不起火）\n超大后排空间（2750mm轴距）\n快充30%-80%：约35分钟',
    },
    {
        'chepinpai': '零跑',
        'chexinghao': 'C11',
        'jiage': '14.98-20.98万',
        'xiaoliang': 8600,
        'shigulv': 2.0,
        'xuhang': 650,
        'dianchileixing': '磷酸铁锂/三元锂',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-11-12',
        'jianjie': '零跑C11中型SUV，14.98万起+650km续航+三联屏座舱，以"半价Model Y"的高性价比策略切入市场。',
        'canshu': '【基本参数】\n车身尺寸：4750×1905×1675mm | 轴距：2930mm\n电机功率：200/400kW（后驱/四驱）\n0-100km/h加速：7.9/4.5秒\n电池容量：69.2/89.97kWh\n续航：502/650km（CLTC）\n\n【配置亮点】\n10.25+12.8+10.25英寸三联屏\n高通8295芯片 | Face ID人脸识别\nLeapmotor Pilot智驾系统',
    },
    {
        'chepinpai': '阿维塔',
        'chexinghao': '12 增程版',
        'jiage': '27.88-34.88万',
        'xiaoliang': 5600,
        'shigulv': 1.2,
        'xuhang': 1100,
        'dianchileixing': '磷酸铁锂',
        'cheshenleixing': '轿车',
        'shangshishijian': '2025-05-15',
        'jianjie': '阿维塔12增程版，华为DriveONE增程系统+ADS 3.0智驾，将华为技术精髓与新能源完美结合。',
        'canshu': '【基本参数】\n车身尺寸：5020×1999×1460mm | 轴距：3020mm\n增程器：1.5T 四缸\n电机功率：230kW\n纯电续航：230km（CLTC）\n综合续航：1100km（CLTC）\n\n【华为配置】\n华为ADS 3.0高阶智驾（192线激光雷达）\n华为DriveONE增程系统\n鸿蒙智能座舱\n3颗激光雷达（全向感知）',
    },
    {
        'chepinpai': '方程豹',
        'chexinghao': '豹5 云辇版',
        'jiage': '28.98-35.28万',
        'xiaoliang': 7200,
        'shigulv': 1.4,
        'xuhang': 1200,
        'dianchileixing': '磷酸铁锂刀片电池',
        'cheshenleixing': '硬派越野SUV',
        'shangshishijian': '2025-04-05',
        'jianjie': '方程豹豹5云辇版，四轮独立驱动+云辇-X智能车身控制+原地掉头，以革命性技术重新定义硬派越野。',
        'canshu': '【基本参数】\n车身尺寸：4750×1930×1900mm | 轴距：2800mm\n增程器：1.5T 143kW\n系统综合功率：505kW\n0-100km/h加速：4.8秒\n纯电续航：125km（CLTC）\n综合续航：1200km（CLTC）\n\n【核心科技】\n云辇-X四轮独立驱动\n原地掉头 | 敏捷转向\n三把差速锁+智能越野模式\n云辇-P智能液压车身控制',
    },
    {
        'chepinpai': '宝马',
        'chexinghao': 'iX3 (新一代)',
        'jiage': '39.99-49.99万',
        'xiaoliang': 4500,
        'shigulv': 1.0,
        'xuhang': 800,
        'dianchileixing': '三元锂电池（4695圆柱）',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2025-06-01',
        'jianjie': '宝马Neue Klasse平台首款量产车，第六代eDrive+800V快充+800km续航，传统豪华品牌的电动化"背水一战"。',
        'canshu': '【基本参数】\n车身尺寸：4755×1920×1660mm | 轴距：2865mm\n电机功率：230/400kW（后驱/四驱）\n0-100km/h加速：6.0/3.8秒\n电池容量：84.6kWh\n续航：600/800km（WLTP）\n\n【BMW技术】\n第六代eDrive电驱技术\n4695规格圆柱形电池\n全景HUD横贯仪表台\n全新iDrive 10系统+大语言模型AI语音',
    },
    {
        'chepinpai': '奔驰',
        'chexinghao': 'EQE SUV',
        'jiage': '43.80-56.98万',
        'xiaoliang': 2800,
        'shigulv': 0.9,
        'xuhang': 613,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2024-10-22',
        'jianjie': '奔驰EQE SUV，EVA纯电平台+10°后轮转向+柏林之声音响，传统豪华品牌电动SUV的标杆之作。',
        'canshu': '【基本参数】\n车身尺寸：4880×2032×1679mm | 轴距：3030mm\n电机功率：215/300kW（后驱/四驱）\n电池容量：96.1kWh\n续航：613/558km（CLTC）\n\n【豪华配置】\nMBUX超联屏（12.3+17.7+12.3英寸）\n10°后轮转向（转弯直径10.7m）\nBurmester 3D环绕音响\n空气悬架+自适应减震',
    },
    {
        'chepinpai': '大众',
        'chexinghao': 'ID.4 X (小鹏合作款)',
        'jiage': '18.99-26.99万',
        'xiaoliang': 7600,
        'shigulv': 1.5,
        'xuhang': 650,
        'dianchileixing': '三元锂电池',
        'cheshenleixing': 'SUV',
        'shangshishijian': '2025-06-15',
        'jianjie': '大众与小鹏联合开发的量产电动SUV，大众品质+小鹏智驾，15-25万级市场的新选择。',
        'canshu': '【基本参数】\n车身尺寸：4650×1920×1680mm | 轴距：2890mm\n电机功率：200/315kW（后驱/四驱）\n0-100km/h加速：6.5/4.2秒\n电池容量：82kWh\n续航：570/650km（CLTC）\n\n【合作亮点】\n小鹏XNGP智驾（高速+城市NOA）\n大众MEB+平台 | 大众底盘调校\nAR-HUD增强现实抬头显示\nIQ.Light矩阵大灯',
    },
]

def generate_engagement():
    return {
        'thumbsupnum': random.randint(0, 500),
        'crazilynum': random.randint(0, 30),
        'clicknum': random.randint(100, 10000),
        'storeupnum': random.randint(0, 100),
        'totalscore': round(random.uniform(3.0, 5.0), 1),
        'discussnum': random.randint(0, 50),
    }

def main():
    print("=" * 60)
    print("  汽车信息数据生成器")
    print(f"  {len(CARS)} 款车型")
    print("=" * 60)

    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM qichexinxi")
    conn.commit()
    print("\n[清空] qichexinxi 旧数据已删除")

    inserted = 0
    for i, car in enumerate(CARS):
        data = {}
        data['chepinpai'] = car['chepinpai']
        data['chexinghao'] = car['chexinghao']
        data['jiage'] = car['jiage']
        data['tupian'] = random.choice(PICTURE_POOL)
        data['xiaoliang'] = car['xiaoliang']
        data['shigulv'] = car['shigulv']
        data['xuhang'] = car['xuhang']
        data['dianchileixing'] = car['dianchileixing']
        data['cheshenleixing'] = car['cheshenleixing']
        data['shangshishijian'] = car['shangshishijian']
        data['jianjie'] = car['jianjie']
        data['canshu'] = car['canshu']
        data['addtime'] = datetime.now()

        eng = generate_engagement()
        data.update(eng)

        cols = ', '.join(data.keys())
        qmarks = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO qichexinxi ({cols}) VALUES ({qmarks})"

        try:
            cursor.execute(sql, tuple(data.values()))
            conn.commit()
            inserted += 1
            print(f"  [{inserted:02d}] {data['chepinpai']} {data['chexinghao']} | {data['jiage']} | 月销{data['xiaoliang']}辆 | 事故率{data['shigulv']}%")
        except Exception as e:
            print(f"  [ERROR] {e}")
            conn.rollback()

    conn.close()

    print("\n" + "=" * 60)
    print(f"  完成！共插入 {inserted} 款车型")
    print("=" * 60)

if __name__ == '__main__':
    main()
