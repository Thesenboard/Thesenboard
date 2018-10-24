from django.shortcuts import render, redirect
from start.serializers import *
from rest_framework import generics
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from django.http import Http404
from rest_framework import status
from django.contrib.auth import login
from start.forms import RegistrationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class HomeView(TemplateView):
    def get(self, request):
        return render(request, 'home.html')


class ProfileView(TemplateView):
    def get(self, request):
        return render(request, 'profile.html')


class RegisterView(TemplateView):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})


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

'''
class UserExtrasDetail(generics.RetrieveAPIView, UpdateModelMixin):
    serializer_class = UserExtrasSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        current_user = request.user
        user = UserExtras.objects.get(identifier=current_user.username)
        data = UserExtrasSerializer(user).data
        return Response(data)
'''