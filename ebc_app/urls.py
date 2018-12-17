from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name = "homeViewName"),
	path("<int:page_no>", views.homepage, name = "homePageViewName"),
	path("search", views.searchome, name = "searchomeViewName"),
	path("<str:search_text>/<int:page_no>/", views.search_page, name = "searchPageViewName"),
	# path("<int:from>/<int:to>/", views.get_home, name = "getHomeViewName"),
]