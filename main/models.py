#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shouji=models.CharField ( max_length=255,null=False, unique=False, verbose_name='手机' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    status=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='状态' )
    '''
    zhanghao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    shouji=VARCHAR
    touxiang=Text
    status=Integer
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class autohome(BaseModel):
    __doc__ = u'''autohome'''
    __tablename__ = 'autohome'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255, null=True, unique=False, verbose_name='标题' )
    imgurl=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    neirong=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    xqurl=models.TextField   (  null=True, unique=False, verbose_name='详情链接' )
    zuozhe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作者' )
    fbtime=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布时间' )
    alltext=models.TextField   (  null=True, unique=False, verbose_name='全文' )
    liulan=models.IntegerField  (  null=True, unique=False, verbose_name='浏览量(万)' )
    fbaddress=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布地点' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    totalscore=models.FloatField   (  null=True, unique=False,default='0', verbose_name='评分' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    title=VARCHAR
    imgurl=Text
    neirong=Text
    xqurl=Text
    zuozhe=VARCHAR
    fbtime=VARCHAR
    alltext=Text
    liulan=Integer
    fbaddress=VARCHAR
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    totalscore=Float
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'autohome'
        verbose_name = verbose_name_plural = '新能源资讯'
class zixunfenlei(BaseModel):
    __doc__ = u'''zixunfenlei'''
    __tablename__ = 'zixunfenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    zixunfenlei=models.CharField ( max_length=255,null=False,unique=True, verbose_name='资讯分类' )
    '''
    zixunfenlei=VARCHAR
    '''
    class Meta:
        db_table = 'zixunfenlei'
        verbose_name = verbose_name_plural = '资讯分类'
class xingyezixun(BaseModel):
    __doc__ = u'''xingyezixun'''
    __tablename__ = 'xingyezixun'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    zixunbiaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='资讯标题' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    zixunfenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='资讯分类' )
    faburen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    fabushijian=models.DateField   (  null=True, unique=False, verbose_name='发布时间' )
    jianjie=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    zixunneirong=models.TextField   (  null=True, unique=False, verbose_name='资讯内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    totalscore=models.FloatField   (  null=True, unique=False,default='0', verbose_name='评分' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    zixunbiaoti=VARCHAR
    fengmian=Text
    zixunfenlei=VARCHAR
    faburen=VARCHAR
    fabushijian=Date
    jianjie=Text
    zixunneirong=Text
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    totalscore=Float
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'xingyezixun'
        verbose_name = verbose_name_plural = '行业资讯'
class zixunjiedu(BaseModel):
    __doc__ = u'''zixunjiedu'''
    __tablename__ = 'zixunjiedu'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    zixunbiaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='资讯标题' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    zixunfenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='资讯分类' )
    faburen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    jiedushijian=models.DateField   (  null=True, unique=False, verbose_name='解读时间' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    jieduneirong=models.TextField   (  null=True, unique=False, verbose_name='解读内容' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    zixunbiaoti=VARCHAR
    fengmian=Text
    zixunfenlei=VARCHAR
    faburen=VARCHAR
    jiedushijian=Date
    zhanghao=VARCHAR
    xingming=VARCHAR
    jieduneirong=Text
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'zixunjiedu'
        verbose_name = verbose_name_plural = '资讯解读'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    title=VARCHAR
    introduction=Text
    picture=Text
    content=Text
    name=VARCHAR
    headportrait=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '系统公告'
class chat(BaseModel):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    adminid=models.BigIntegerField  (  null=True, unique=False, verbose_name='管理员id' )
    ask=models.TextField   (  null=True, unique=False, verbose_name='提问' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复' )
    isreply=models.IntegerField  (  null=True, unique=False, verbose_name='是否回复' )
    isread=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='已读/未读(1:已读,0:未读)' )
    uname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    uimage=models.TextField   (  null=True, unique=False, verbose_name='用户头像' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='内容类型(1:文本,2:图片,3:视频,4:文件,5:表情)' )
    '''
    userid=BigInteger
    adminid=BigInteger
    ask=Text
    reply=Text
    isreply=Integer
    isread=Integer
    uname=VARCHAR
    uimage=Text
    type=Integer
    '''
    class Meta:
        db_table = 'chat'
        verbose_name = verbose_name_plural = 'ai问答'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='外键id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class users(BaseModel):
    __doc__ = u'''users'''
    __tablename__ = 'users'



    __authTables__={}
    __authPeople__ = '是'
    __isAdmin__ = '是'
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    username=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
    password=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    role=models.CharField ( max_length=255, null=True, unique=False,default='管理员', verbose_name='角色' )
    image=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    username=VARCHAR
    password=VARCHAR
    role=VARCHAR
    image=Text
    '''
    class Meta:
        db_table = 'users'
        verbose_name = verbose_name_plural = '管理员'
class discussautohome(BaseModel):
    __doc__ = u'''discussautohome'''
    __tablename__ = 'discussautohome'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    score=models.FloatField   (  null=True, unique=False, verbose_name='评分' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    score=Float
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussautohome'
        verbose_name = verbose_name_plural = '新能源资讯'
class discussxingyezixun(BaseModel):
    __doc__ = u'''discussxingyezixun'''
    __tablename__ = 'discussxingyezixun'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    score=models.FloatField   (  null=True, unique=False, verbose_name='评分' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    score=Float
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussxingyezixun'
        verbose_name = verbose_name_plural = '行业资讯评论'

class qichexinxi(BaseModel):
    __doc__ = u'''qichexinxi'''
    __tablename__ = 'qichexinxi'

    __authTables__={}
    __authPeople__='否'
    __sfsh__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    chepinpai=models.CharField(max_length=255, null=True, unique=False, verbose_name='汽车品牌')
    chexinghao=models.CharField(max_length=255, null=True, unique=False, verbose_name='车型型号')
    jiage=models.CharField(max_length=255, null=True, unique=False, verbose_name='价格区间')
    tupian=models.TextField(null=True, unique=False, verbose_name='图片')
    xiaoliang=models.IntegerField(null=True, unique=False, default='0', verbose_name='月销量')
    shigulv=models.FloatField(null=True, unique=False, default='0', verbose_name='事故率(%)')
    xuhang=models.IntegerField(null=True, unique=False, default='0', verbose_name='续航里程(km)')
    dianchileixing=models.CharField(max_length=255, null=True, unique=False, verbose_name='电池类型')
    cheshenleixing=models.CharField(max_length=255, null=True, unique=False, verbose_name='车身类型')
    shangshishijian=models.DateField(null=True, unique=False, verbose_name='上市时间')
    jianjie=models.TextField(null=True, unique=False, verbose_name='简介')
    canshu=models.TextField(null=True, unique=False, verbose_name='详细参数')
    thumbsupnum=models.IntegerField(null=True, unique=False, default='0', verbose_name='赞')
    crazilynum=models.IntegerField(null=True, unique=False, default='0', verbose_name='踩')
    clicktime=models.DateTimeField(auto_now=True, null=True, unique=False, verbose_name='最近点击时间')
    clicknum=models.IntegerField(null=True, unique=False, default='0', verbose_name='点击次数')
    discussnum=models.IntegerField(null=True, unique=False, default='0', verbose_name='评论数')
    totalscore=models.FloatField(null=True, unique=False, default='0', verbose_name='评分')
    storeupnum=models.IntegerField(null=True, unique=False, default='0', verbose_name='收藏数')
    '''
    chepinpai=VARCHAR
    chexinghao=VARCHAR
    jiage=VARCHAR
    tupian=Text
    xiaoliang=Integer
    shigulv=Float
    xuhang=Integer
    dianchileixing=VARCHAR
    cheshenleixing=VARCHAR
    shangshishijian=Date
    jianjie=Text
    canshu=Text
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    totalscore=Float
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'qichexinxi'
        verbose_name = verbose_name_plural = '汽车信息'
