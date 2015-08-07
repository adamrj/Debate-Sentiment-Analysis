from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^sentiment/', include('sentiment.urls', namespace='sentiment')),
    url(r'^admin/', include(admin.site.urls)),
]
