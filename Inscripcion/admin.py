from django.contrib import admin

from .models import Carrera
from .models import Estudiante
from .models import Curso
from .models import Matricula


# Register your models here.
admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)