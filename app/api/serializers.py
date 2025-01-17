from rest_framework import serializers 
from api.models import Todo

class AdminTodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id',
                'title',
                'description',
                'completed')


class UserTodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id',
                'title',
                'description')
