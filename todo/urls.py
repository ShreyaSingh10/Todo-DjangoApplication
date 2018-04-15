from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [
	url(r'^$', include('work.urls')),
	url(r'^work/', include('work.urls')),
    url(r'^admin/', admin.site.urls),
]
