from django.shortcuts import render

# Create your views here.
class ShoppingSquareView(APIView):
    # 购物商城-广场视图
    def get(self, request):
        return Response({"message": "Hello, World!"})   