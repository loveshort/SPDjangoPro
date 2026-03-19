from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "shopping_login"

router = DefaultRouter()
# 之前计划注册的 ViewSet，在这里保留示例写法（当前没有真正启用）
# router.register(r"shopping_login", views.ShoppingListViewSet, basename="shopping_login")

urlpatterns = [
    # 简单的 REST 风格登录信息接口（当前实际生效的接口）
    path("logins/", views.ShoppingLoginListCreate.as_view(), name="login-list"),
    path(
        "logins/<int:pk>/",
        views.ShoppingLoginRetrieveUpdateDestroy.as_view(),
        name="login-detail",
    ),
    # 之前写的基于 router 的路由，先保留为注释，避免报错
    # path("", include(router.urls)),
]