from rest_framework import serializers

from .models import Post, Comment
from rest_framework.reverse import reverse
from rest_framework.settings import api_settings
from atividade4.settings import baseurl

class PostSerializerList(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(
        source='comments.count',
        read_only=True
    )
    url = serializers.SerializerMethodField('get_post')

    def get_post(self, obj):
        url = reverse('post-user-detail', args=(obj.perfil.id,obj.id))
        request = self.context.get('request')
        base = "http://" + "127.0.0.1:8000"
        # print(request.META['HTTP_HOST'])
        return base + url



    class Meta:
        model = Post
        fields = ('id', 'title', 'comment_count','url')

class CommentsListSerializer(serializers.ModelSerializer):

    post = PostSerializerList(many=False, read_only=True)
    # post = PostSerializerList(view_name="post-user-detail", read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'name','email','body','post')
