from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:total>/choose/", views.choose, name="choose"),
    path("generate/", views.generate_timetable, name="generate"),
    path("generate/download/", views.download_timetable, name="download_timetable"),
]