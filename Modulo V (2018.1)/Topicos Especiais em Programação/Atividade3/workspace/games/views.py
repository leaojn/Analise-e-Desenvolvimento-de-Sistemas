"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework import generics
from rest_framework import generics, status, mixins as drf_mixins, exceptions, authentication

from .models import Game, Score, Player, GameCategory
from .serializers import GameSerializer, ScoreSerializer, PlayerSerializer,GameCategorySerializer


# @api_view(['GET', 'POST'])
# def game_list(request):
#     if request.method == 'GET':
#         games = Game.objects.all()
#         games_serializer = GameSerializer(games, many=True, context={'request': request})
#         return Response(games_serializer.data)
#     elif request.method == 'POST':
#         game_serializer = GameSerializer(data=request.data)
#
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def game_detail(request, pk):
#     try:
#         game = Game.objects.get(pk=pk)
#     except Game.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         games_serializer = GameSerializer(game)
#         return Response(games_serializer.data)
#
#     if request.method == 'PUT':
#         game_serializer = GameSerializer(game, data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data)
#         return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         if game.release_date < timezone.now():
#             raise ValidationError('Somente jogos que ainda não foram lançados pode ser excluidos',
#                                   code=status.HTTP_400_BAD_REQUEST)
#         game.delete()
#
#     return Response(status=status.HTTP_204_NO_CONTENT)
#

class game_category_list(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'

class game_category_detail(drf_mixins.DestroyModelMixin, drf_mixins.ListModelMixin,
                              drf_mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = GameCategory.objects.all()

        return Response(status=status.HTTP_200_OK,
                        data=GameCategorySerializer(queryset, many=True, context={'request': request}).data)

    def delete(self, request, *args, **kwargs):
        queryset = GameCategory.objects.all()

        try:
            favorite = queryset.get(venue__pk=self.kwargs.get('pk'))
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            raise exceptions.NotFound(detail=('A categoria aoo'))

class game_list(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'

class game_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'

class player_list(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'

class player_detail(generics.RetrieveDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'

class score_list(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-list'

class score_detail(generics.RetrieveDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-detail'


