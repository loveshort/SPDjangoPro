
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'shopping_login'

router = DefaultRouter()
router.login('shopping_login', views.ShoppingLoginModel, basename='shopping_login')
 
 urlpatterns = [

 ] + router.urls