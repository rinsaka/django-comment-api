from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'title', 'body', 'updated_at']

    # def validate(self, data):
    #     if len(data['title']) > 10:
    #         raise serializers.ValidationError("タイトルの最大文字数は10文字です")
    #     if len(data['body']) > 15:
    #         raise serializers.ValidationError("本文の最大文字数は15文字です")
    #     return data

    def validate_title(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("タイトルの最大文字数は10文字です")
        return value

    def validate_body(self, value):
        if len(value) > 15:
            raise serializers.ValidationError("本文の最大文字数は15文字です")
        return value
