__author__ = 'vikas.pwr86@gmail.com'

"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from app_ecommerce import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login', views.Login.as_view(), name='login'),
    url(r'^api/logout', views.logout),
    url(r'^api/category$', views.Categories.as_view(), name='category'),
    url(r'^api/subcategory$', views.SubCategories.as_view(), name='subcategory'),
    url(r'^api/supplier$', views.Suppliers.as_view(), name='supplier'),
    url(r'^api/product$', views.Products.as_view(), name='product'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
