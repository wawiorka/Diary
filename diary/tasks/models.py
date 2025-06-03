from enum import Enum

from django.db import models
from django.utils import timezone
from notifications.handlers import send_message

from users.models import User
from diary import settings
from notifications.models import Notification as BaseNotification


# Create your models here.
class Goal(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='goals', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    execution_date = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    goal = models.ForeignKey(Goal, related_name='tasks', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     goal = Goal.objects.get(goal=self.goal)
    #     if goal.is_completed == "True":
    #         self.is_completed = "True"
    #         return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class NotificationsTypes(Enum):
    NEW_NOTE = 'NEW_NOTE'

# create a signal on create new goal
# from django.db.models.signals import post_save, m2m_changed
# from django.dispatch import receiver
#

# это сигнал для обновления выполнения задач при выполнении цели
# но потом я его в сериалайзер перенесла
# @receiver(m2m_changed, sender=Goal.is_completed)
# def completed_tasks(sender, created, instance, action, **kwargs):
#     if action is "goal_add" and instance.is_completed == True:
#         tasks = Task.objects.filter(goal=instance.id)
#         for task in tasks:
#             task.is_completed = True
#             task.save()

# @receiver(post_save, sender=Goal)  # это сигнал для уведомления о создании новой задачи
# def create_goal(sender, instance, created, **kwargs):
#     if created:
#         # send notification
#         send_message(f'Напоминание', instance.author, NotificationsTypes.NEW_NOTE.value)



# для себя
# class NotificationType(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Notification(BaseNotification):
#     recipient = models.ForeignKey(User, on_delete=models.CASCADE)
#     notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ['-timestamp']

