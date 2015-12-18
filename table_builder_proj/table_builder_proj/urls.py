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
# Table Builder:
from django.conf.urls import include, url
from django.contrib import admin
# Importing main page View and original Page View
from table_builder.views import AccountView, TestOriginalView
# Importing views for CRUD functions
from table_builder.views import AccountCreate, AccountUpdate, AccountDelete
# Importing Django REST Framework ViewSet
from table_builder.viewsets import AccountViewSet
# Django REST Framework ViewSet Routing:
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'Account', AccountViewSet)

# Tree View:
from tree_view.views import TreeView
# Importing Django REST Framework ViewSet
from tree_view.viewsets import TreeNodeViewSet
router.register(r'TreeNode', TreeNodeViewSet)

urlpatterns = [
    # Django Admin Site:
    url(r'^admin/', admin.site.urls),
    # Django REST Framework API site:
    url(r'^api/v1/', include(router.urls), name='api'),
    # Main Page
    url(r'^$', AccountView.as_view(), name='main'),
    # Original table-builder Page
    url(r'^orig', TestOriginalView.as_view(), name='orig'),
    # Create new account
    url(r'^create', AccountCreate.as_view(success_url = '/create'), name='create'),
    # Update existing account information
    url(r'^update', AccountUpdate.as_view(), name='update'),
    # Delete account
    url(r'^delete', AccountDelete.as_view(), name='delete'),
    # Tree view page
    url(r'^tree', TreeView.as_view(), name='tree')

]
