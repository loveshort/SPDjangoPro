from django.db import models

# Create your models here.
class ShoppingMineModel(models.Model):
    """
    购物商城-我的模型类
    """
    # 用户id
    user_id = models.CharField(max_length=100, verbose_name="用户id")
    # 手机号
    phone = models.CharField(max_length=11, verbose_name="手机号")
    #购物商城-产品标题
    title = models.CharField(max_length=100, verbose_name="标题")
    #原价格
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="原价格")
    #现价格
    current_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="现价格")
    #折扣
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="折扣")
    #图片
    image = models.ImageField(upload_to='image/', default='',verbose_name="图片")
    #创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    #更新时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    def __str__(self):
        return self.username