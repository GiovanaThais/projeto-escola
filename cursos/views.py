from django.db.models import query
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404 
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import filters
from rest_framework.filters import SearchFilter

''' API V1 - VERSAO 1 '''

class CursosAPIView(generics.ListCreateAPIView):
    queryset= Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Curso.objects.all()
    serializer_class = CursoSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo'] #filtro de pesquisa
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset= Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id= self.kwargs.get('curso_pk'),pk = self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


'''API VERSAO 2 (V2)'''

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo'] #filtro de pesquisa
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'curso'] #filtro de pesquisa
