from rest_framework import serializers
from core.models import Jogador
class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ('id', 'nome', 'image','nacionalidade','altura','idade')