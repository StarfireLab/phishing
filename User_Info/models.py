from django.utils import timezone
from django.db import models

# Create your models here.


class click(models.Model):
    email = models.CharField("邮箱", max_length=200, blank=True, null=True )
    ip = models.CharField("IP", max_length=200, blank=True, null=True)
    created_at = models.DateTimeField("创建时间", default=timezone.now)

    class Meta:
        verbose_name = '邮件点击率统计'
        verbose_name_plural = '邮件点击率统计'


class email_info(models.Model):
    email = models.CharField("邮箱", max_length=200, blank=True, null=True)
    password = models.CharField("密码", max_length=200, blank=True, null=True)
    new_password1 = models.CharField("新密码1", max_length=200, blank=True, null=True)
    new_password2 = models.CharField("新密码2", max_length=200, blank=True, null=True)

    created_at = models.DateTimeField("创建时间", default=timezone.now)
    updated_at = models.DateTimeField("更新时间", default=timezone.now)

    class Meta:
        verbose_name = '邮箱账号密码信息'
        verbose_name_plural = '邮箱账号密码信息'

