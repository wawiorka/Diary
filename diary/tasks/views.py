from django.contrib.admin import action
from django.shortcuts import render
from django.views.generic import UpdateView
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task, Goal
from tasks.serializers import TaskSerializer, GoalSerializer, GoalAddSerializer

from tasks.serializers import GoalCompletedSerializer, TaskCompletedSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):  # CRUD
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user).order_by('id')


class TaskCompletedView(viewsets.ModelViewSet):  # используется только UPDATE
    serializer_class = TaskCompletedSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user).order_by('id')


class GoalViewSet(viewsets.ModelViewSet):  # используется только READ
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(author=user).order_by('id')


class GoalAddViewSet(viewsets.ModelViewSet):  # используется только C.UD, без READ
    serializer_class = GoalAddSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(author=user).order_by('id')


class GoalCompletedView(APIView):  # используется только UPDATE

    def put(self, request, *args, **kwargs):
        user = self.request.user
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Goal.objects.filter(author=user).get(pk=pk)
            # tasks = Task.objects.filter(goal=instance.id)
        except:
            return Response({"error": "Object does not exists"})

        serializer = GoalCompletedSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"goal": serializer.data})

    # для себя
    # def get_queryset(self):
    #     user = self.request.user
    #     return Goal.objects.filter(author=user).order_by('id')

    # def partial_update(self, request, *args, **kwargs):
    #     partial = True
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     return Response(serializer.data)

    # def update_tasks(self, instance, validated_data):
    #     user = self.request.user
    #     if instance.is_completed == "True":
    #         instance.save()

    # @action(detail=True, methods=["put"], name="Change Password")
    # def update_tasks(self, instanse, request, id):
    #     goal = Goal.objects.get(id=id)
    #     if request.method == 'PUT' and goal.is_completed == "True":
    #         tasks = Task.objects.filter(goal=Goal.id).order_by('id')
    #         for task in tasks:
    #             task.is_completed = "True"
    #             task.save()


            # if goal.is_completed == "True":