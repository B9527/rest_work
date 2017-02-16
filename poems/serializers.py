# coding:utf-8

from rest_framework import serializers
from .models import Poem, Poet


class PoetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = ['name', 'dynasty', 'brief', 'alias', ]


class PoemSerializer(serializers.ModelSerializer):
    author = PoetSerializer()

    class Meta:
        model = Poem
        fields = ['author', 'content', 'title', 'type']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        if len(Poet.objects.filter(**author_data))==0:
            author = Poet.objects.create(**author_data)
        else:
            author = Poet.objects.get(**author_data)
        poem = Poem.objects.create(author=author, **validated_data)
        return poem

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        if len(Poet.objects.filter(**author_data))==0:
            author = Poet.objects.create(**author_data)
        else:
            author = Poet.objects.get(**author_data)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.type = validated_data.get('type', instance.type)
        instance.author = author
        instance.save()
        return instance
