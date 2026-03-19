from rest_framework import generics, permissions
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.response import Response

from .models import ShoppingLoginModel
from .serializers import ShoppingLoginSerializer


class ShoppingLoginListCreate(generics.ListCreateAPIView):
    """
    GET: 返回所有登录记录
    POST: 创建一条新的登录记录
    """

    queryset = ShoppingLoginModel.objects.all()
    serializer_class = ShoppingLoginSerializer
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )
    permission_classes = (permissions.AllowAny,)


class ShoppingLoginRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: 获取单条记录
    PUT/PATCH: 更新
    DELETE: 删除
    """

    queryset = ShoppingLoginModel.objects.all()
    serializer_class = ShoppingLoginSerializer
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )
    permission_classes = (permissions.AllowAny,)


# ===== 以下为之前写的 DRF 示例/练习代码备份，已注释掉防止报错 =====
#
# from tokenize import Token
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
# from rest_framework import generics, status, viewsets, permissions
# from .permissions import IsOwnerOrReadOnly
# from .serializers import ShoppingLoginSerializer, ShoppingLoginCreateSerializer
# from .models import ShoppingLoginModel, Course
#
# def generate_token(sender, instance=None, created=False, **kwargs):
#     """
#     创建用户时自动生成token
#     """
#     if created:
#         Token.objects.create(user=instance)
#
# """
# 一，函数式编程 Function Based View
# """
#
# @api_view(["GET", "POST"])
# @authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))
# @permission_classes((permissions.IsAuthenticated,))
# def course_list(request):
#     """
#     获取所有的课程信息或新增一个课程
#     """
#     if request.method == "GET":
#         s = CourseSerializer(Course.objects.all(), many=True)
#         return Response(data=s.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         s = CourseSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(data=s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(["GET", "PUT", "DELETE"])
# @authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))
# @permission_classes((permissions.IsAuthenticated,))
# def course_detail(request, pk):
#     """
#     获取、更新、删除一个课程
#     """
#     try:
#         course = Course.objects.get(pk=pk)
#     except Course.DoesNotExist:
#         return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         s = CourseSerializer(instance=course)
#         return Response(data=s.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         s = CourseSerializer(instance=course, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(data=s.data, status=status.HTTP_200_OK)
#         return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# """
# 二，类视图 Class Based View
# """
#
# class CourseList(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request):
#         queryset = ShoppingLoginModel.objects.all()
#         s = ShoppingLoginSerializer(queryset, many=True)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         s = ShoppingLoginSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(data=s.data, status=status.HTTP_201_CREATED)
#         return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class CourseDetail(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     @staticmethod
#     def get_object(pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             return None
#
#     def get(self, request, pk):
#         obj = self.get_object(pk)
#         if not obj:
#             return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
#         s = ShoppingLoginSerializer(instance=obj)
#         return Response(s.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         obj = self.get_object(pk)
#         if not obj:
#             return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
#         s = ShoppingLoginSerializer(instance=obj, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(data=s.data, status=status.HTTP_200_OK)
#         return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         obj = self.get_object(pk)
#         if not obj:
#             return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# """
# 三 通用类视图，Generic Class Based View
# """
#
# class GShoppingList(generics.ListCreateAPIView):
#     queryset = ShoppingLoginModel.objects.all()
#     serializer_class = ShoppingLoginCreateSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
# class GShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ShoppingLoginModel.objects.all()
#     serializer_class = ShoppingLoginSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
#
# """
# 四、DRF 的视图集 viewsets
# """
#
# class ShoppingListViewSet(viewsets.ModelViewSet):
#     queryset = ShoppingLoginModel.objects.all()
#     serializer_class = ShoppingLoginSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
#
#     def perform_create(self, serializer):
#         serializer.save(teacher=self.request.user)
