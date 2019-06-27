
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Login import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 
# router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/' , views.login, name = 'login' ),
    path('ulogin/', auth_views.LoginView.as_view(template_name = 'Login/login.html'),name = 'ulogin'),
    path('logout/' , auth_views.LogoutView.as_view(template_name = 'Login/logout.html'), name = 'logout' ),
    path('register/' , views.register, name = 'register' ),
    path('',views.index, name='index'),
    path('test/', views.test),
    path('r/', include(router.urls))
]
