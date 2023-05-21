from rest_framework.serializers import ModelSerializer
from main.models import Blog

class BlogLiSer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author']


class BlogDetSer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


