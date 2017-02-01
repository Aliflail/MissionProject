
from django.conf.urls import url
from django.contrib import admin
from registration.views import HomeView, IndexView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(), name='home'),
    url(r'^$',IndexView.as_view(),name='index')
 	#url(r'^register/$',RegisterView.as_view(), name='register'),
    # url(r'^login/$',LoginView, name='login'),
    # url(r'^logout/$',LogoutView, name='logout'),
]