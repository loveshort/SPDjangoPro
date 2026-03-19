from django.db import models


class ShoppingLoginModel(models.Model):
    """
    购物商城-登录模型类
    """
    # 用户id
    user_id = models.CharField(max_length=100, verbose_name="用户id")
    # 手机号
    phone = models.CharField(max_length=11, verbose_name="手机号")
    # 用户名
    username = models.CharField(max_length=100, verbose_name="用户名")
    # 密码
    password = models.CharField(max_length=100, verbose_name="密码")
    # 头像
    avatar = models.ImageField(upload_to="avatar/", default="", verbose_name="头像")
    # 昵称
    nickname = models.CharField(max_length=100, verbose_name="昵称")
    # 签名
    signature = models.CharField(max_length=100, verbose_name="签名")
    # 性别
    sex = models.CharField(max_length=10, verbose_name="性别")
    # 生日
    birthday = models.DateField(verbose_name="生日")
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "登录信息"
        verbose_name_plural = verbose_name
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.username


# ===== 以下为之前的示例/练习代码备份，只保留做参考，不参与运行 =====
# 原来这里还定义过一个内嵌的 Course 模型，并且引入了一些未使用/拼写有误的字段，
# 会在导入 models 时直接报错。为避免影响项目启动，这里仅作为注释备份。
#
# from math import trunc
# from tabnanny import verbose
# from django.conf import settings
#
# class Course(models.Model):
#     name = models.CharField(
#         max_length=255,
#         unique=True,
#         help_text="课程名称",
#         verbose_name="名称",
#     )
#     introduction = models.TextField(
#         help_text="课程简介",
#         verbose_name="简介",
#     )
#     teacher = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         help_text="课程讲师",
#         verbose_name="讲师",
#     )
#     price = models.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         help_text="课程价格",
#         verbose_name="价格",
#     )
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
#
#     class Meta:
#         verbose_name = "信息"
#         verbose_name_plural = verbose_name
#         ordering = ("price",)
#
#     def __str__(self):
#         return self.name

