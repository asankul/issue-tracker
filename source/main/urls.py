"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import IndexView, TodoView, ToDoListCreateView, ToDoListUpdateView, ToDoListDeleteView, StatusCreateView, StatusView, StatusUpdateView, StatusDeleteView, TypeView, TypeCreateView, TypeUpdateView, TypeDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('lists/<int:pk>/', TodoView.as_view(), name='list_view'),
    path('lists/create', ToDoListCreateView.as_view(), name='list_add'),
    path('list/<int:pk>/edit/', ToDoListUpdateView.as_view(), name='list_update'),
    path('list/<int:pk>/delete/', ToDoListDeleteView.as_view(), name='list_delete'),
    path('lists/status', StatusView.as_view(), name='statuses'),
    path('lists/status/create', StatusCreateView.as_view(), name='status_add'),
    path('list/status/<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    path('list/status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('lists/type', TypeView.as_view(), name='types'),
    path('lists/type/create', TypeCreateView.as_view(), name='type_add'),
    path('list/type/<int:pk>/edit/', TypeUpdateView.as_view(), name='type_update'),
    path('list/type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
]
