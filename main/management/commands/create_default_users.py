from datetime import datetime
from django.core.management.base import BaseCommand
from main.models import users, yonghu


class Command(BaseCommand):
    help = '创建默认管理员账号和前台测试用户'

    def handle(self, *args, **options):
        # 管理员
        if not users.objects.filter(username='admin').exists():
            users.objects.create(
                username='admin',
                password='admin',
                role='管理员',
                addtime=datetime.now(),
            )
            self.stdout.write(self.style.SUCCESS('[OK] 管理员 admin/admin 已创建'))
        else:
            self.stdout.write('[跳过] 管理员已存在')

        # 前台用户 001~008
        names = ['马超', '张嘉怡', '李思远', '林书豪', '孙伟', '赵子轩', '王强', '徐婷']
        genders = ['男', '男', '男', '男', '男', '女', '女', '男']
        phones = ['13290652385', '13189065234', '15065432109', '13138842380',
                  '15187985612', '13023456789', '13654321098', '13890489621']

        created = 0
        for i, (name, gender, phone) in enumerate(zip(names, genders, phones)):
            account = '{:03d}'.format(i + 1)
            if not yonghu.objects.filter(zhanghao=account).exists():
                yonghu.objects.create(
                    zhanghao=account,
                    mima='123456',
                    xingming=name,
                    xingbie=gender,
                    shouji=phone,
                    addtime=datetime.now(),
                )
                created += 1

        if created:
            self.stdout.write(self.style.SUCCESS(
                '[OK] {} 个前台用户已创建 (001~008 / 123456)'.format(created)))
        else:
            self.stdout.write('[跳过] 前台用户已存在')
