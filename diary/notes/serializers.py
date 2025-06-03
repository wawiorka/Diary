from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ["author"]


    def create(self, validated_data):
        user = self.context["request"].user
        note = Note.objects.create(**validated_data, author=user)
        return note

    def update(self, instance, validated_data):
        user = self.context["request"].user
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
