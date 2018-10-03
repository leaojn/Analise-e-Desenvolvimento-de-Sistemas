from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tep import permissions
from .models import Post, Comment
from .serializers import PostSerializerList, CommentsListSerializer


# Create your views here.

class posts_user(APIView):
    permission_classes = (
        permissions.ReadOnly,
        IsAuthenticated
    )

    def get_object(self, pk):
        return Post.objects.filter(perfil_id=pk)

    """
       List all snippets, or create a new snippet.
       """

    def get(self, request, pk, format=None):
        posts = self.get_object(pk)
        serializer = PostSerializerList(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        permission_classes = (
            permissions.IsOwnerOrReadOnly,
            IsAuthenticated
        )
        serializer = PostSerializerList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializerList(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class posts_user_detail(APIView):
    permission_classes = (
        permissions.IsOwnerOrReadOnly,
        IsAuthenticated
    )

    def get_object(self, pk, post_id):
        return Post.objects.get(perfil_id=pk, id=post_id)

    """
       List all snippets, or create a new snippet.
       """

    def get(self, request, pk, post_id, format=None):
        posts = self.get_object(pk, post_id)
        serializer = PostSerializerList(posts)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializerList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, post_id, format=None):
        posts = self.get_object(pk, post_id)
        serializer = PostSerializerList(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, post_id, format=None):
        posts = self.get_object(pk, post_id)
        comments = posts.comments.all()
        for c in comments:
            c.delete()
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class comment_list(APIView):

    def get_object(self, pk, post_id):
        return Comment.objects.filter(post__perfil_id=pk, post_id=post_id)

    """
       List all snippets, or create a new snippet.
       """

    def get(self, request, pk, post_id, format=None):
        comments = self.get_object(pk, post_id)
        serializer = CommentsListSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, post_id, format=None):
        comment = self.get_object(pk, post_id)
        serializer = CommentsListSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, post_id, format=None):
        post = self.get_object(pk, post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class posts_comment_detail(APIView):
    permission_classes = (
        permissions.ReadOnly,
        IsAuthenticated
    )

    def get_object(self, pk, post_id, comment_id):
        return Comment.objects.get(post__perfil_id=pk, post_id=post_id, id=comment_id)

    """
       List all snippets, or create a new snippet.
       """

    def get(self, request, pk, post_id, comment_id, format=None):
        posts = self.get_object(pk, post_id, comment_id)
        serializer = CommentsListSerializer(posts)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, post_id, comment_id, format=None):
        posts = self.get_object(pk, post_id, comment_id)
        serializer = CommentsListSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, post_id, comment_id, format=None):
        posts = self.get_object(pk, post_id, comment_id)
        comments = posts.comments.all()
        for c in comments:
            c.delete()
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
