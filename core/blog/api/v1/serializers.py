from rest_framework import serializers
from blog.models import Post,Category
from accounts.models import Profile
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
        read_only_fields = ["content","author"]
        
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
        rep["category"] = CategorySerializer(instance.category,context={"request":request}).data
        return rep
    def create(self, validate_date):
        validate_date["author"]=Profile.objects.get(user__id = self.context.get("request").user.id)
        return super().create(validate_date)
    
    def update(self, instance, validate_date):
        return super().update(instance, validate_date)