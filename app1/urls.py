from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('demand', views.demand_page),
    path('geography', views.geography_page),
    path('skills', views.skills_page),
    path('vacancies', views.vacancies_page),
]