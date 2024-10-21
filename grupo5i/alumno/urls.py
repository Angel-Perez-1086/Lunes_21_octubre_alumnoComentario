from django.urls import path
from alumno import views

urlpatterns = [
    path('', views.index_vista, name='index_vista'),
    path('Alumno/<int:id>',views.Alumno_vista,name='Alumno_vista')
]