from django.db import models

# Create your models here.


class User(models.Model):
    """
    用户模型类
    用于存储系统用户的基本信息
    """
    # 用户名，最大长度100字符
    username = models.CharField(max_length=100, verbose_name="用户名")
    
    # 邮箱，必须唯一，用于登录或找回密码
    email = models.EmailField(unique=True, default='',verbose_name="邮箱")
    
    # 密码，存储加密后的密码
    password = models.CharField(max_length=100, verbose_name="密码")
    
    # 创建时间，记录用户注册的时间，自动设置为当前时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    # 更新时间，记录用户最后一次修改信息的时间，每次保存自动更新
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    # 用户性别
    gender = models.CharField(max_length=10, verbose_name="性别",default='男')
    # 用户年龄
    age = models.IntegerField(verbose_name="年龄",default=0)
    # 用户手机号
    phone = models.CharField(max_length=11, verbose_name="手机号",default='')
    # 用户地址
    address = models.CharField(max_length=100,default='',verbose_name="地址")
    # 用户头像
    avatar = models.ImageField(upload_to='avatar/', default='',verbose_name="头像")

    def __str__(self):
        """
        返回对象的字符串表示，在后台管理界面显示用户名
        """
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
