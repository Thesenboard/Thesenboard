from django.shortcuts import render
from django.contrib.auth.models import User
from start.serializers import UserSerializer
from rest_framework import generics
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from django.http import Http404
from rest_framework import status


class HomeView(TemplateView):
    def get(self, request):
        return render(request, 'home.html')


class ProfileView(TemplateView):
    def get(self, request):
        return render(request, 'profile.html')


class UserDetail(generics.RetrieveAPIView, UpdateModelMixin):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        data = UserSerializer(user).data
        return Response(data)

    def put(self, request):
        current_user = request.user
        user = self.get_queryset(current_user.id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





