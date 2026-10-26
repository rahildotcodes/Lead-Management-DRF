"""
URL configuration for LeadManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from leadApp import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lead',views.LeadCreateListView.as_view(),name="lead_view"),
    path('lead/detail/<int:pk>',views.LeadRetrieveUpdateDeleteView.as_view(),name="lead_update_view"),
    path('token',auth_view.obtain_auth_token)
    # path('lead/status',views.StatusLevelLeadsView.as_view(),name="lead_status_view"),
]
