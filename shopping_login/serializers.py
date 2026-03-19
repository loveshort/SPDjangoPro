from rest_framework import serializers
from .models import ShoppingLoginModel
from django import forms
from django.contrib.auth.models import User

class ShoppingLoginForm(forms.ModelForm):
    class Meta:
        model = ShoppingLoginModel
        fields = ("username", "email", "password")


class ShoppingLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingLoginModel
        fields = '__all__'

class ShoppingLoginCreateSerializer(serializers.ModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')  # 外键字段 只读
    class Meta:
        model = ShoppingLoginModel #写法和上面的shoppingLoginForm类似
        #exclude = ('id',) #注意元组中只有1个元素时不能写成("id")
        #fields = ('id','name','introduction','teacher','price','created_at','updated_at')
        fields = '__all__'
        depth = 2

class ShoppingLoginUpdateSerializer(serializers.HyperlinkedModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')

    class Meta:
        model = ShoppingLoginModel
        #url是默认值，可在settings.py中设置URL_FIELD_NAME使全局生效

        fields = '__all__'
        # fields = ('id','url','name','introduction','teacher','price','created_at','updated_at')