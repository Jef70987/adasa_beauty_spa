from rest_framework import serializers
from .models import*

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientComment
        fields = '__all__'
