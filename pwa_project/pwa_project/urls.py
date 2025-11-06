"""
URL configuration for pwa_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from tasks import views as task_views
from .views import serve_service_worker

urlpatterns = [
    path('admin/', admin.site.urls),
	path('users/', include(("users.urls", "users"), namespace="users")),
	path('tasks/', include(("tasks.urls", "tasks"), namespace="tasks")),
    path('accounts/', include('allauth.urls')),
    path('', task_views.index, name='home'),
    path('service-worker.js', serve_service_worker, name='service_worker'),

]
