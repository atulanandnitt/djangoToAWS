"""projectToAWS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from app_to_upload.views import FilePolicyAPI, FileUploadCompleteHandler


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='upload.html'), name='upload-home'),
    url(r'^admin/', admin.site.urls),
    url(r'^upload/$', TemplateView.as_view(template_name='upload.html'), name='upload-home'),
    url(r'^api/files/complete/$', FileUploadCompleteHandler.as_view(), name='upload-complete'),
    url(r'^api/files/policy/$', FilePolicyAPI.as_view(), name='upload-policy'),

]


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
