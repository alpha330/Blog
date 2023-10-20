from rest_framework import serializers
from blog.models import Post,Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["name","id"]
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url",read_only=True)
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["id","title","updated_date","snippet","published_date","status","relative_url","author","category","content","image","absolute_url"]
        read_only_fields = ["content"]
        
    def get_absolute_url(self,obj):
        request= self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    def to_representation(self,instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop("snippet",None)
            rep.pop("absolute_url",None)
            rep.pop("relative_url",None)
        else :
            rep.pop("content",None)
            
        rep["category"] = CategorySerializer(instance.category).data
        
        return rep