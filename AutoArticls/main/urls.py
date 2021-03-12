from .import views
from django.urls import path


app_name = 'main'

urlpatterns = [
	path('', views.index, name = "home"),
	path('<int:article_id>/', views.detail, name = "detail"),
	path('<int:article_id>/leave_comment/', views.leave_comment, name = "leave_comment"),
]