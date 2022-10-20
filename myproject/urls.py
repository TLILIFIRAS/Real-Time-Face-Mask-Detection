
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from facemaskdetection import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.index,name="Homepage"),
    path('video_feed', views.video_feed, name='video_feed'),
    path('mask_feed', views.mask_feed, name='mask_feed'),

]
