import re
from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse
from django.http import JsonResponse

from .models import Curso
from .models import Estudiante
from .models import Carrera
from .serializers import CarreraSerializer, CursoSerializer, EstudianteSerializer

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
# Create your views here.


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer


@api_view(["GET"])
def estudiantes_carnet_identidad(request,ci):
    """
    Estudiantes filtrados por Carnet de identidad
    """
    try:
        estudiantes = Estudiante.objects.filter(ci=ci)
        return JsonResponse(
            EstudianteSerializer(estudiantes,many=True).data,
            safe=False,
            status = 200
        )

    except Exception as e:
        return JsonResponse({"mensaje": str(e)},status=400)
