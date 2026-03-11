from django.db import models

# Create your models here.
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
    avatar = models.ImageField(upload_to='avatar/', default='',verbose_name="头像")
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

    def __str__(self):
        return self.username
    class Meta:
        app_label = "shopping_login"