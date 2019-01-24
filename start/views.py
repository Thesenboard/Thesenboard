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
from .models import These, ThesisEntries, ThesisAbstimmung
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
       thesisAbstimmung = ThesisAbstimmung.objects.filter(thesisAbstimmungsId=thesis_id)
       thesisUser = User.objects.get(username=thesis.thesenUserId)

       if(thesisUser.user_visibility == "name"):
            userName = thesisUser.first_name + ' ' + thesisUser.last_name
       elif (thesisUser.user_visibility == "benutzername"):
           userName = thesisUser.username
       else:
           userName = "Anonym"

       countPositives = 0
       countAll = 0
       for t in thesisAbstimmung:
           countAll += 1
           if t.thesisAbstimmungsEntscheidung:
               countPositives += 1
       return render(request, 'thesis.html', {'thesis': thesis, 'thesisEntries': thesisEntries, 'status': status,
                                              'countAll': countAll, 'countPositives': countPositives, 'userId': request.user.id, 'userName': userName})

    def post(self, request, thesis_id):
        thesis = These.objects.get(pk=thesis_id)
        status = self.getStatus(thesis)
        form = ThesisEntryForm(request.POST)
        thesisAbstimmung = ThesisAbstimmung.objects.filter(thesisAbstimmungsId=thesis_id)
        thesisUser = User.objects.get(username=thesis.thesenUserId)

        if (thesisUser.user_visibility == "name"):
            userName = thesisUser.first_name + ' ' + thesisUser.last_name
        elif (thesisUser.user_visibility == "benutzername"):
            userName = thesisUser.username
        else:
            userName = "Anonym"
        countPositives = 0
        countAll = 0
        for t in thesisAbstimmung:
            countAll += 1
            if t.thesisAbstimmungsEntscheidung:
                countPositives += 1
        if form.is_valid():
            entry = form.save(commit=False)
            entry.thesisEntriesUserId = request.user
            entry.save()
            entry.thesisEntriesThese.add(thesis.thesenId)
            entry.save()
            thesisEntries = ThesisEntries.objects.all().filter(thesisEntriesThese__thesenId=thesis_id)
            return render(request, 'thesis.html', {'thesis': thesis, 'thesisEntries': thesisEntries, 'status': status,
                                              'countAll': countAll, 'countPositives': countPositives, 'userId': request.user.id, 'userName': userName})
        else:
            thesisEntries = ThesisEntries.objects.all().filter(thesisEntriesThese__thesenId=thesis_id)
            return render(request, 'thesis.html', {'thesis': thesis, 'thesisEntries': thesisEntries, 'status': status, 'form': form,
                                              'countAll': countAll, 'countPositives': countPositives, 'userId': request.user.id, 'userName': userName})


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
        data = self.serializer_class(user).data
        return Response(data)

    def put(self, request):
        current_user = request.user
        user = self.get_queryset(current_user.id)
        serializer = self.serializer_class(user, data=request.data, partial=True)
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
        data = self.serializer_class(thesen).data
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
        data = self.serializer_class(entries, many=True).data
        return Response(data)


class ThesenAbstimmungView(viewsets.ModelViewSet):
    serializer_class = ThesenAbstimmungSeralizer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None, userId=None):
        try:
            t = ThesisAbstimmung.objects.filter(thesisAbstimmungsId__thesenId=pk)
            t = t.filter(thesisAbstimmungsUser=userId)
            return t
        except These.DoesNotExist:
            raise Http404

    def list(self, request, pk=None):
        thesenAbstimmung = self.get_queryset(pk=pk, userId=request.user.id)
        data = self.serializer_class(thesenAbstimmung, many=True).data
        return Response(data)

    def put(self, request, pk=None):
        thesenAbstimmung = self.get_queryset(pk=pk, userId=request.user.id)
        for abstimmung in thesenAbstimmung:
            if abstimmung.thesisAbstimmungsUser == request.user:
                return Response("none")
        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        instance = self.get_queryset(pk=pk, userId=request.user.id)
        serializer = self.serializer_class(instance.first(), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



