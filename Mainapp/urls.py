from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendrier/', views.calendrier, name='calendrier'),
    path('nostalgie/', views.nostalgie, name='nostalgie'),
    path('nostalgie/<int:nostalgie_id>/', views.nostalgie_detail, name='nostalgie_detail'),
    path('concert/<int:concert_id>/', views.concert_detail, name='concert_detail'),
    path('actualite/<int:actualite_id>/', views.actualite_detail, name='actualite_detail'),
    path('search_result/', views.search_result, name='search_result'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
