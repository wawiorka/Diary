from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import NoteViewSet

router = DefaultRouter()
router.register(r'', NoteViewSet, basename='notes')

urlpatterns = [
    path('notes/', include(router.urls)),
]

# router = DefaultRouter()
# router.register(r'users', UserViewSet, 'user')
# urlpatterns = router.urls