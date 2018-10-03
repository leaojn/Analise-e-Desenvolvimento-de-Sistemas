from django.shortcuts import render
from rest_framework import viewsets
from core.models import Jogador
from core.serializers import JogadorSerializer
# Create your views here.
class JogadorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer