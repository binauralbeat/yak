from django.conf.urls import url

from . import views

app_name = "yktrkr"
urlpatterns = [
    url(r'^$', views.user_view.index, name='index'),
    url(r'^login$', views.user_view.login_user, name='login'),
    url(r'^levels$', views.water_lev_view.water_levels, name='levels')

]