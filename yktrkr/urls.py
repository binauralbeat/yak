from django.conf.urls import url

from . import views

app_name = "yktrkr"
urlpatterns = [
    url(r'^$', views.user_view.index, name='index'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^login$', views.user_view.login_user, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^levels$', views.water_lev_view.water_levels, name='levels'),
    url(r'^launch$', views.boat_launch_view.boat_ramps, name='launch'),
    url(r'^favorites$', views.favorites_view.fav, name='favorites'),
    url(r'^favorite_list$', views.favorites_view.favs_post, name='favorite_list'),


]