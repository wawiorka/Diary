from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GoalViewSet, TaskViewSet, GoalAddViewSet, GoalCompletedView, TaskCompletedView

router = DefaultRouter()
router.register(r'goals', GoalViewSet, basename='goals')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'goal_cud', GoalAddViewSet, basename='goals_cud')
# router.register(r'goal', GoalCompletedView, basename='goal_completed')
# router.register(r'goal', GoalCompletedView.as_view(), basename="goal_completed")
router.register(r'task', TaskCompletedView, basename='task_completed')

urlpatterns = [
    path('', include(router.urls)),
    path('goal/<int:pk>/', GoalCompletedView.as_view(), name="goal_completed"),
        # path('notifications/', include('notifications.urls', namespace='notifications')),
]