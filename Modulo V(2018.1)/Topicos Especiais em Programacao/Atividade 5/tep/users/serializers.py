from rest_framework import serializers

from tep.serializers import PostSerializerList
from users.models import Perfil


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id','name','user','email')


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id', 'name', 'email', 'city', 'zipcode', 'street', 'suite', 'phone',)


class UserSerializerDetailandPost(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='detail-profile', read_only=True)

    post = PostSerializerList(many=True, read_only=True)
    # post = PostSerializerList(view_name="post-user-detail", read_only=True)

    class Meta:
        model = Perfil
        fields = ('url','id', 'name', 'email', 'post')


class UserSerializerPost(serializers.ModelSerializer):
    post = PostSerializerList(source='posts', many=True)
    # post = PostSerializerList(view_name="post-user-detail", read_only=True)
    # post = serializers.HyperlinkedIdentityField(so,view_name='post-user-detail', read_only=True, many=True)

    class Meta:
        model = Perfil
        fields = ('id', 'name', 'email', 'city', 'zipcode', 'street', 'suite', 'phone', 'post')

class UserCountDetail(serializers.ModelSerializer):
    total_posts = serializers.IntegerField(
        source='posts.count',
        read_only=True
    )
    total_comments = serializers.IntegerField(
        source='comments',
        read_only=True
    )

    class Meta:
        model = Perfil
        fields = ('id', 'name', 'total_posts','total_comments')
