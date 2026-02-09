from django.db import models

# Create your models here.

class LoginModel(models.Model):
    """
    登录模型类
    用于存储登录用户的基本信息
    """
    # 用户名，最大长度100字符
    username = models.CharField(max_length=100, verbose_name="用户名")
    
    # 密码，存储加密后的密码
    password = models.CharField(max_length=100, verbose_name="密码")
    
    # 创建时间，记录用户登录的时间，自动设置为当前时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    # 更新时间，记录用户最后一次登录的时间，每次保存自动更新
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        """
        返回对象的字符串表示，在后台管理界面显示用户名
        """
        return self.username

    class Meta:
        verbose_name = "登录"
        verbose_name_plural = verbose_name