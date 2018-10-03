from rest_framework import serializers
from rest_framework import status
from .models import Game, Score, Player, GameCategory
from rest_framework.validators import UniqueTogetherValidator
# from django.utils.datetime_safe import datetime
import datetime
class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCategory
        fields = ('url','pk','name','games')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),slug_field='pk')
    def validate(self, data):
        for dado in data:
            if data[dado] == "":
                raise serializers.ValidationError("algum dos campos esta vazio, verifique os dados enviados!",
                                                  code=status.HTTP_400_BAD_REQUEST)
        return data

    class Meta:
        model = Game
        fields = ('url','id', 'name', 'release_date', 'game_category')

    validators = [
        UniqueTogetherValidator(
            queryset=Game.objects.all(),
            fields=('name', ),
            message =('Jogos não podem ter nomes repetidos')
        )
    ]

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(),
                                 slug_field='pk')
    player = serializers.SlugRelatedField(queryset=Player.objects.all(),
                                 slug_field='pk')

    def validate(self, data):
       if data['game'] is None or data['player'] is None:
           raise serializers.ValidationError("O Game ou o Player não foi informado",
                                             code=status.HTTP_400_BAD_REQUEST)
       elif data['game'] is None and data['player'] is None:
           raise serializers.ValidationError("O Game e o Player não foram informado",
                                             code=status.HTTP_400_BAD_REQUEST)
       elif data['score'] < 0 or data['score'] is None:
           raise serializers.ValidationError("Informe valores maiores que zero ou informe algum valor",
                                                 code=status.HTTP_400_BAD_REQUEST)
       elif data['score_data'] > datetime.date.today():
           raise serializers.ValidationError("Data invalida",
                                                 code=status.HTTP_400_BAD_REQUEST)


       return data

    class Meta:
        model = Score
        fields = ('url','pk','score','player','game','score_data' )

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        fields = (
        'url',
        'name',
        'gender',
        'scores',
        )