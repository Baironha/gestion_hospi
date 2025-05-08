from .models        import pacientes, especialidades, doctores,citas, especialidades_x_doctores
from rest_framework import serializers


class pacientes_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = pacientes # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class especialidades_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = especialidades # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class doctores_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = doctores # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class especialidades_x_doctores_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = especialidades_x_doctores # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class citas_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = citas # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB





