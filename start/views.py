from django.shortcuts import render, redirect
from start.serializers import *
from rest_framework import generics
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from django.http import Http404
from rest_framework import status, viewsets
from django.contrib.auth import login
from .forms import RegistrationForm
from .forms import ThesisForm, ThesisEntryForm
from .models import These, ThesisEntries
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
User = get_user_model()
import datetime
from django.shortcuts import get_object_or_404


class HomeView(TemplateView):
    def get(self, request):
        thesen = These.objects.all()
        return render(request, 'home.html', {'thesen': thesen})


class ProfileView(TemplateView):
    def get(self, request):
        return render(request, 'profile.html')


class NewThesisView(TemplateView):
    def get(self, request):
        return render(request, 'new_thesis.html')

    def post(self, request):
        form = ThesisForm(request.POST)
        if form.is_valid():
            these = form.save(commit=False)
            these.thesenUserId = request.user
            these.save()
            return redirect('home')
        return render(request, 'new_thesis.html', {'form': form})


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


class ThesisView(TemplateView):
    def get(self, request, thesis_id):
       thesis = These.objects.get(pk=thesis_id)
       status = self.getStatus(thesis)
       thesisEntries = ThesisEntries.objects.filter(thesisEntriesThese__thesenId=thesis_id)
       return render(request, 'thesis.html', {'thesis': thesis, 'thesisEntries': thesisEntries, 'status': status})

    def post(self, request, thesis_id):
        thesis = These.objects.get(pk=thesis_id)
        status = self.getStatus(thesis)
        form = ThesisEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.thesisEntriesUserId = request.user
            entry.save()
            entry.thesisEntriesThese.add(thesis.thesenId)
            entry.save()
            thesisEntries = ThesisEntries.objects.all().filter(thesisEntriesThese__thesenId=thesis_id)
            return render(request, 'thesis.html', {'thesis': thesis, 'thesisEntries': thesisEntries, 'status': status})
        else:
            thesisEntries = ThesisEntries.objects.all().filter(thesisEntriesThese__thesenId=thesis_id)
            return render(request, 'thesis.html', {'thesis': thesis, 'thesisEntries': thesisEntries, 'status': status, 'form': form})

    def getStatus(self, thesis):
        endDate = datetime.date(thesis.thesenTime.year, thesis.thesenTime.month,
                                thesis.thesenTime.day) + datetime.timedelta(days=90)
        nowDate = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month,
                                datetime.datetime.now().day)
        if (endDate < nowDate):
            return 'geschlossen'
        return 'offen'

'''
APIS ###################################################################
'''


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
        user = self.get_queryset(id=current_user.id)
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


class AllThesenView(viewsets.ModelViewSet):
    serializer_class = ThesenSeralizer

    def get_queryset(self):
        try:
            return These.objects.all().order_by('-thesenId')
        except These.DoesNotExist:
            raise Http404

    def get(self, request):
        thesen = self.get_queryset()
        data = ThesenSeralizer(thesen).data
        return Response(data)


class ThesisEntryView(viewsets.ModelViewSet):
    serializer_class = ThesisEntriesSeralizer

    def get_queryset(self, pk=None):
        try:
            entries = ThesisEntries.objects.all().filter(thesisEntriesThese__thesenId=pk)
            return entries
        except These.DoesNotExist:
            raise Http404

    def list(self, request, pk=None):
        queryset = self.get_queryset(pk=pk)
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page')
        entries = paginator.page(page)
        data = ThesisEntriesSeralizer(entries, many=True).data
        return Response(data)

