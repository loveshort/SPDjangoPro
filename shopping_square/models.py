from django.db import models

# Create your models here.
class ShoppingSquareModel(models.Model):
    """
    购物商城-广场模型类
    """
    # 用户id
    user_id = models.CharField(max_length=100, verbose_name="用户id")
    # 手机号
    phone = models.CharField(max_length=11, verbose_name="手机号")
    # 标题
    title = models.CharField(max_length=100, verbose_name="标题")
    # 原价格
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="原价格")
    # 现价格
    current_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="现价格")
    # 折扣
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="折扣")
    # 图片
    image = models.ImageField(upload_to='image/', default='',verbose_name="图片")
    # 描述
    description = models.TextField(verbose_name="描述")
    #发货地
    shipping_address = models.CharField(max_length=100, verbose_name="发货地")
    # 快递费
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="快递费")
    #销量
    sales_volume = models.IntegerField(default=0, verbose_name="销量")
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")