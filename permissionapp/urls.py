from django.urls import path

from permissionapp import views

app_name= 'permissionapp'

urlpatterns = [
    path("demo/", views.Demo.as_view(),name='demo'),
    path("user/", views.UserAPIView.as_view(),name='user'),
]
