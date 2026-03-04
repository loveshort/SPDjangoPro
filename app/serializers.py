from rest_framework import serializers
from .models import AppModel

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppModel
        #全部字段
        #只读字段
        # read_only_fields = ['id', 'pub_time']
        # #写入字段
        # write_only_fields = ['name', 'title', 'author', 'price' ]
        # #排除字段 
        # exclude = ['id', 'pub_time']
        # #嵌套字段
        # nested_fields = {
        #     'author': AuthorSerializer(),
        # }
        fields = '__all__'