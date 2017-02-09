
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^home/',views.HomeView.as_view(),name="home"),
    url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^register/$',views.RegisterView.as_view(), name='register'),
    url(r'^login/',views.loginview.as_view(),name='login'),
    url(r'^logout/',views.logoutview,name="logout"),
    url(r'^test/(?P<test_id>[0-9]+)/$',views.TestView.as_view(),name="test"),
    url(r'^qtest/(?P<test_id>[0-9]+)/$',views.TestQuestionView.as_view(),name="qtest"),
    url(r'^compilertest/',views.Compilerq.as_view(),name='name'),
    url(r'^profile/',views.profileview,name='profile')
]