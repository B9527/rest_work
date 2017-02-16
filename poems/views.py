from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PoemSerializer
from .models import Poem


# Create your views here.

class PoemListView(APIView):
    def get(self, request, format=None):
        poems = Poem.objects.all()
        serialzer = PoemSerializer(poems, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        seriailzer = PoemSerializer(data=request.data, many=True)
        if seriailzer.is_valid():
            seriailzer.save()
            return Response(seriailzer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seriailzer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def poem_detail(request, pk):
    try:
        poem = Poem.objects.get(pk=pk)
    except Poem.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PoemSerializer(poem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PoemSerializer(poem, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        poem.delete()
        return Response(status.HTTP_204_NO_CONTENT)
