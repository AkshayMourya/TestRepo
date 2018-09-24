from rest_framework import serializers
from .models import blog_post
class blog_serializer(serializers.ModelSerializer):
    class Meta:
        model = blog_post
        fields = ('id','title', 'description', 'created_by', 'created_at')
