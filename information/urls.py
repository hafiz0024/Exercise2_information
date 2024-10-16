from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getvalue/", views.getvalue, name="getvalue"),
    path("getvalue/save_data", views.save_data, name="save_data"),
    path("view/", views.view, name="view"),
    path("database/", views.database, name="database"),
    path("course/", views.course, name="course"),
    path("course/search_course/", views.search_course, name="search_course"),
    path("course/update_course/<str:code>", views.update_course, name="update_course"),
    path("course/update_course/save_update_course/<str:code>", views.save_update_course, name="save_update_course"),
    path("course/delete_course/<str:code>", views.delete_course, name="delete_course"),
   ]
