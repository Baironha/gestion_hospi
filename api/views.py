from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import pacientes, especialidades, doctores, citas,especialidades_x_doctores
from .serializer import pacientes_Serializer, especialidades_Serializer, doctores_Serializer, citas_Serializer,especialidades_x_doctores_Serializer

class pacientes_ListCreateView(ListCreateAPIView):
    queryset         = pacientes.objects.all()
    serializer_class = pacientes_Serializer

class pacientes_DetailView(RetrieveUpdateDestroyAPIView):
    queryset         = pacientes.objects.all()
    serializer_class = pacientes_Serializer


class especialidades_ListCreateView(ListCreateAPIView):
    queryset         = especialidades.objects.all()
    serializer_class = especialidades_Serializer

class especialidades_DetailView(RetrieveUpdateDestroyAPIView):
    queryset         = especialidades.objects.all()
    serializer_class = especialidades_Serializer


class doctores_ListCreateView(ListCreateAPIView):
    queryset         = doctores.objects.all()
    serializer_class = doctores_Serializer

class doctores_DetailView(RetrieveUpdateDestroyAPIView):
    queryset         = doctores.objects.all()
    serializer_class = doctores_Serializer



class especialidades_x_doctores_ListCreateView(ListCreateAPIView):
    queryset         = especialidades_x_doctores.objects.all()
    serializer_class = especialidades_x_doctores_Serializer

class especialidades_x_doctores_DetailView(RetrieveUpdateDestroyAPIView):
    queryset         = especialidades_x_doctores.objects.all()
    serializer_class = especialidades_x_doctores_Serializer


class citas_ListCreateView(ListCreateAPIView):
    queryset         = pacientes.objects.all()
    serializer_class = pacientes_Serializer

class citas_DetailView(RetrieveUpdateDestroyAPIView):
    queryset         = citas.objects.all()
    serializer_class = citas_Serializer


