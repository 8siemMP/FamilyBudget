"""FamilyBudget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from budgets.views import BudgetViewSet, PrivilegeManagementViewSet
from categories.views import CategoryViewSet
from entries.views import EntryViewSet
from users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'budgets', BudgetViewSet, basename='budget')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'entries', EntryViewSet, basename='entry')

urlpatterns = [
    path('', include(router.urls)),
    path('budgets/<int:budget_pk>/privileges/<int:user_pk>/',
         PrivilegeManagementViewSet.as_view(actions={
             'get': 'retrieve',
             'delete': 'destroy',
             'post': 'create'
         })),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
