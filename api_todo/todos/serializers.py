from os import read

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Todo

class TodoSerializer (ModelSerializer):
    # status = serializers.SerializerMethodField()
    # title = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['id', 'title', 'description', 'created_at', 'edited_at', 'status']
    
    # def get_status(self, todo: Todo):
        # return int(todo.status)
        # return todo.get_status_display()
    
    # def get_title(self, todo: Todo):
        # return todo.title.upper()

    # def get_user(self, todo: Todo):
    #     return {
    #         'id': todo.user.id,
    #         'username': todo.user.username,
    #         'email': todo.user.email
    #     }

    def to_representation(self, todo: Todo):
        return {
            'id': todo.id,
            'title': todo.title.upper(),
            'description': todo.description,
            'created_at': todo.created_at,
            'edited_at': todo.edited_at,
            'status': todo.get_status_display(),
            'user': {
                'id': todo.user.id,
                'username': todo.user.username,
                'email': todo.user.email
            }
        }