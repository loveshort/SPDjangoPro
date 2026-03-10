from django.shortcuts import render

# Create your views here.
class ShoppingMineView(APIView):
    # 购物商城-我的视图
    def get(self, request):
        return Response({"message": "Hello, World!"})   