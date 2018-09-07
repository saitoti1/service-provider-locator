"""mozio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from service_area.views import CompanySRUD, CompanyCMRL, ServiceAreaCMR, ServiceAreaSRUD, SearchServiceArea

urlpatterns = [
    path('company/', CompanyCMRL.as_view(), name='company-create-multipleRetrive-login'),
    path('my-company/', CompanySRUD.as_view(), name='company-singleRetrive-update-delete'),
    path('service-area/', ServiceAreaCMR.as_view(), name='service-area-create-multipleRetrive-search'),
    path('my-service-area/<uuid:service_area_id>/',
         ServiceAreaSRUD.as_view(), name='service-area-singleRetrive-update-delete'),
    path('search/', SearchServiceArea.as_view(), name='search-service-area')
]
