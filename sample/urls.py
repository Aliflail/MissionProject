
from django.conf.urls import url
from django.contrib import admin
from registration.views import HomeView, IndexView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(), name='home'),
 	url(r'^index/$',IndexView.as_view(), name='index'),      
]