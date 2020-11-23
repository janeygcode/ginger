from django.urls import path
from . import views


urlpatterns = [
	path("", views.stuff_index, name="stuff_index"),
	path("waf", views.waf_stuff_index, name="waf_stuff_index"),
	path("<int:pk>/", views.stuff_detail, name="stuff_detail"),
	path("search/", views.search, name="search"),
	]