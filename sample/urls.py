
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('registration.urls')),
    # url(r'^logout/$',LogoutView, name='logout'),
]