from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router =DefaultRouter()
router.register(r"Cursos",views.CursoViewSet)
router.register(r"Estudiantes",views.EstudianteViewSet)
router.register(r"Carrera",views.CarreraViewSet)


urlpatterns = [
    path('estudiantes/buscar/<str:ci>',views.estudiantes_carnet_identidad),
    path('',include(router.urls))
]