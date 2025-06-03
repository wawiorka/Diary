from django.contrib.admin import action
from rest_framework import serializers
from .models import Task, Goal
from diary import settings


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'is_completed', 'goal']

    def create(self, validated_data):
        user = self.context["request"].user
        task = Task.objects.create(
            author=user,
            title=validated_data['title'],
            goal=validated_data['goal'])
        return task


class TaskCompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['is_completed']


class GoalSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Goal
        fields = ['id', 'title', 'is_completed', 'tasks']


class GoalAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'is_completed']

    def create(self, validated_data):
        user = self.context["request"].user
        goal = Goal.objects.create(
            author=user,
            title=validated_data['title'])
        return goal


class GoalCompletedSerializer(serializers.ModelSerializer):
    # tasks = TaskCompletedSerializer(many=True)
    class Meta:
        model = Goal
        fields = ['is_completed']

    def update(self, instance, validated_data):
        # user = self.context["request"].user
        instance.is_completed=validated_data['is_completed']
        if instance.is_completed:
            tasks = Task.objects.filter(goal=instance.id)
            for task in tasks:
                task.is_completed = True
                task.save()
        return instance