from django.urls import path

from . import views

app_name = 'wines'
urlpatterns = [
    path('', views.index, name='index'),
    path('reds/', views.index_red, name='index_reds'),
    path('whites/', views.index_white, name='index_whites'),
    path('reds/<int:wine_id>/', views.details_red, name='details_reds'),
    path('whites/<int:wine_id>/', views.details_white, name='details_whites'),
]