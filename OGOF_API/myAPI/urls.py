# myapi/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

# router = routers.DefaultRouter()
# router.register(r'developercontacts', views.DeveloperViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
	url(r'^developercontacts/$', views.developer_contacts, name ='developercontacts'),
	url(r'^developerdetail/(?P<id>[0-9]+)/$', views.developer_detail, name ='developerdetail'),
	url(r'^developersearch/$', views.DevSearch.as_view(), name = 'developersearch'),
]