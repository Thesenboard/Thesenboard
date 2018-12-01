from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_visibility = models.CharField(max_length=40)
    user_tags = models.CharField(max_length=255)


class These(models.Model):
    thesenId = models.AutoField(primary_key=True)
    thesenUserId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    thesenTitel = models.CharField(max_length=255)
    thesenArgument = models.TextField()
    thesenFazit = models.TextField()
    thesenTime = models.DateTimeField(auto_now=True)
    thesenQuelle = models.TextField(null=True, blank=True)


class ThesisEntries(models.Model):
    thesisEntriesId = models.AutoField(primary_key=True)
    thesisEntriesUserId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user')
    thesisEntriesTitel = models.CharField(max_length=255)
    thesisEntriesArgument = models.TextField()
    thesisEntriesFazit = models.TextField()
    thesisEntriesTime = models.DateTimeField(auto_now=True)
    thesisEntriesQuelle = models.TextField(null=True, blank=True)
    thesisEntriesThese = models.ManyToManyField(These, related_name='thesisEntriesThese')


class ThesisAbstimmung(models.Model):
    thesisAbstimmungsId = models.ForeignKey(These, null=True, on_delete=models.SET_NULL)
    thesisAbstimmungsUser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    thesisAbstimmungsEntscheidung = models.BooleanField()


class Zwischenruf(models.Model):
    zwischenrufId = models.AutoField(primary_key=True)
    beitragsId = models.ForeignKey(These, on_delete=models.PROTECT)
    beitragsUserId = models.ForeignKey(User, on_delete=models.PROTECT)
    zwischenruf = models.TextField()
    zwischenrufTime = models.DateTimeField(auto_now=True)
