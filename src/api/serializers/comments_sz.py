from project.models import Coment
from rest_framework import serializers



class ComentSerializers(serializers.ModelSerializer):
    author = serializers.CharField(
        read_only=True
    )
    post = serializers.CharField(
    )
    class Meta:
        model = Coment
        fields = '__all__'

class ComentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coment
        fields = '__all__'