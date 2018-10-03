from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.urls import reverse

from tep import permissions
from .models import Perfil
from .serializers import UserSerializerList, UserCountDetail, UserSerializerDetail, UserSerializerDetailandPost, \
    UserSerializerPost


# Create your views here.
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'profiles': reverse('user-list'),
            'profiles-post':reverse('profile-user-list')
        })


class user_list(generics.ListAPIView):
    throttle_scope = 'user-list'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Perfil.objects.all()
    serializer_class = UserSerializerList
    name = 'user-list'
    permission_classes = (
        permissions.ReadOnly,
        IsAuthenticated
    )



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class TokenCustom(ObtainAuthToken):
    throttle_scope = 'token-api'

    throttle_classes = (ScopedRateThrottle,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
        })


class user_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = UserSerializerDetail
    name = 'user-detail'


class profile_user_list(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsOwnerOrReadOnly,
        IsAuthenticated
    )
    queryset = Perfil.objects.all()
    serializer_class = UserSerializerDetailandPost
    name = 'profile-user-list'


class profile_user_detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.ReadOnly,
        IsAuthenticated
    )
    queryset = Perfil.objects.all()
    serializer_class = UserSerializerPost
    name = 'detail-profile'


class user_detail_count(APIView):
    """
       List all snippets, or create a new snippet.
       """

    def get_object(self, pk):
        return Perfil.objects.get(id=pk)

    """
       List all snippets, or create a new snippet.
       """

    def get(self, request, pk, format=None):
        posts = self.get_object(pk)
        serializer = UserCountDetail(posts, )
        return Response(serializer.data)
