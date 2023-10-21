from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,action
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from blog.models import Post,Category
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer,CategorySerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
# views config to send urls.py

# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticated])
# def postlist(request):
#     if request.method == "GET" :
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST" :
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)
    
# class PostList(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     def get(self,request):
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)
        
# @api_view(["GET","PUT","DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_details(request,id):
#     post = get_object_or_404(Post,pk=id,status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer =PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    
# class PostDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
    
#     def get(self,request,id):
#         post = get_object_or_404(Post,pk=id,status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         post = get_object_or_404(Post,pk=id,status=True)
#         serializer =PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,id):
#         post = get_object_or_404(Post,pk=id,status=True)
#         post.delete()
#         return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
        
class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Post.objects.filter(status=True)
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Post.objects.filter(status=True)
    
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'category','status','created_date','updated_date','published_date','status']
    
    @action(methods=["get"],detail=False)
    def get_ok(self,request):
        return Response({"detail":"OK"})

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    queryset = Category.objects.all()
    
