"""
URL configuration for classproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views
from django.conf.urls import include
  
urlpatterns = [
    path("admin/", admin.site.urls),
    path('' , views.index, name = 'index'),
    path('order/' , views.buy_product_view, name = 'order'),
    path('contact/' , views.contact_name_view, name = 'contact'),
    path('shopping_detail/' , views.shopping_detail, name = 'shopping_detail'),  
    path('register/' , views.register_name_view, name = 'register'),  
    path('login/' , views.login_name_view, name = 'login'),  
    path('profile/' , views.profile, name = 'profile'),    
    path('about/' , views.about_us, name = 'about')    
]