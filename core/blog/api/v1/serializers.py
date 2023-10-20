from rest_framework import serializers
from blog.models import Post,Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title","updated_date","published_date","status","author","category","content","image"]
        read_only_fields = ["content"]
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["name","id"]