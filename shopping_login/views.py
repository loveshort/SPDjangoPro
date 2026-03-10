from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ShoppingLoginModel

# Create your views here.
class ShoppingLoginView(APIView):
    # 购物商城-登录视图
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = ShoppingLoginModel.objects.filter(username=username, password=password).first()
        if user:
            return Response({"message": "登录成功"})
        else:
            return Response({"message": "登录失败"})
        return Response({"message": "Hello, World!"})