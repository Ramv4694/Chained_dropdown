"""dropdown URL Configuration

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

from django.conf.urls import url,include
from.import views

app_name = 'countries';

urlpatterns = [
     url(r'^form/$', views.country_list, name="country_list"),
     url(r'^ajaxcall/$', views.Ajaxcall, name="Ajaxcall"),
     url(r'^ajaxcalldistrict/$', views.Ajaxcall_district, name="Ajaxcall_district"),
     url(r'^ajaxcountry/$',views.Ajaxcallcountry,name="Ajaxcallcountry")
]
