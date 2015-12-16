"""table_builder_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
# Importing main page View
from table_builder.views import AccountView
# Importing Django REST Framework ViewSet
from table_builder.viewsets import AccountViewSet
# Django REST Framework ViewSet Routing:
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'Account', AccountViewSet)


urlpatterns = [
    # Django Admin Site:
    url(r'^admin/', admin.site.urls),
    # Django REST Framework API site:
    url(r'^api/v1/', include(router.urls), name='api'),
    # Main Page
    url(r'^$', AccountView.as_view(), name='main'),
]
