"""
URL configuration for crud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('addemp',v.add_emp),
    path('acc',v.add_account),
    path('emplist',v.emp_list),
    path('delete1',v.delete_emp),
    path('delete2/<int:eid>',v.delete2_emp),
    path('edit/<int:eid>',v.edit_emp),
    path('acclist',v.account_list),
    path('acdelete',v.delete_acc),
    path('acdelete2/<int:aid>',v.delete2_acc),
    path('acedit/<int:aid>',v.edit_acc),
]
