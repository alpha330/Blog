from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
# views config to send urls.py

@api_view()
def postlist(request):
    posts = Post.objects.filter(status=True)
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)
@api_view()
def post_details(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data)
    