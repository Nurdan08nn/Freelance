from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'category', CategoryViewSet, basename='categories')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('project/', ProjectListAPIView.as_view(), name='project_list'),
    path('project/<int:pk>', ProjectDetailAPIView.as_view(), name='project_detail'),
]

