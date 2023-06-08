from django.urls import path
from . import views

#lista de URLs playONB
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('empleado/', views.empleado, name='empleado'),
    path('empleado/crear', views.crear, name='crear'),
    path('empleado/editar', views.editar, name='editar'),
 #   path('login/', views.login_view, name='login'),
 #   path('logout/', views.logout_view, name='logout'),
]