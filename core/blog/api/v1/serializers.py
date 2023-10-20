from rest_framework import serializers
from blog.models import Post,Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url",read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(many=False,slug_field="name",queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ["id","title","updated_date","snippet","published_date","status","relative_url","author","category","content","image","absolute_url"]
        read_only_fields = ["content"]
        
    def get_absolute_url(self,obj):
        request= self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    def to_representation(self,instance):
        return super().to_representation(instance)
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["name","id"]