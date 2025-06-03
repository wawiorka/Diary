from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Note
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .serializers import NoteSerializer



# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user).order_by('date_created')


# User = get_user_model()
#
# class NoteViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = NoteSerializer
#
#     def get_queryset(self):
#
#         queryset = super().get_queryset().all().order_by('date_created')
#         return queryset.filter(author=self.request.user)
#
#         if self.request.user.is_authenticated:  # Проверяем пользователь авторизованный или нет
#             return queryset.filter(author=self.request.user)
#         return queryset.filter(category__is_published=True,
#                         is_published=True,
#                         pub_date__lte=timezone.now())


    # queryset = Note.objects.all().order_by('date_created')
    # serializer_class = NoteSerializer


    # def do_note(self, serializer):
    #     serializer.save(author=self.request.user)



# User = get_user_model()
#
# class NoteListView(ListMixin, ListView): model = Note
#     def get_queryset(self):
#         queryset = super().get_queryset().all().order_by('date_created')
#         return queryset.filter(author=self.request.user)

        # if self.request.user.is_authenticated  # Проверяем пользователь авторизованный или нет
        #     return queryset.filter(author=self.request.user)
        # return queryset.filter(category__is_published=True,
        #                     is_published=True,
        #                     pub_date__lte=timezone.now())


# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all().order_by('date_created')
#     serializer_class = NoteSerializer
#     permission_classes = [permissions.IsAuthenticated]
#

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdmin User]
    #     return [permission() for permission in permission_classes]



