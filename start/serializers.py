from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import These, ThesisEntries, User, ThesisAbstimmung


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'user_visibility', 'user_tags')


class ThesenSeralizer(serializers.ModelSerializer):
    class Meta:
        model = These
        fields = ('thesenId', 'thesenUserId', 'thesenTitel', 'thesenArgument', 'thesenFazit', 'thesenTime')


class UserEntriesSerializer(serializers.RelatedField):
    def to_representation(self, value):
        if(value.user_visibility == 'name'):
            username = value.first_name + ' ' + value.last_name
        elif(value.user_visibility == 'anonym'):
            username = 'Anonym'
        else:
            username = value.username
        return username


class ThesisEntriesSeralizer(serializers.ModelSerializer):
    thesisEntriesUserId = UserEntriesSerializer(read_only=True)

    class Meta:
        model = ThesisEntries
        fields = ('thesisEntriesUserId', 'thesisEntriesId', 'thesisEntriesTitel', 'thesisEntriesArgument',
                  'thesisEntriesFazit', 'thesisEntriesTime', 'thesisEntriesQuelle', 'thesisEntriesThese')


class ThesenAbstimmungSeralizer(serializers.ModelSerializer):
    class Meta:
        model = ThesisAbstimmung
        fields = '__all__'

