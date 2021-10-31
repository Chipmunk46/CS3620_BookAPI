from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Horror')
    serializer_class = BookSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Comedy')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Romance')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Mystery')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fantasy')
    serializer_class = BookSerializer


class HistoricalViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Historical')
    serializer_class = BookSerializer


class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='ScienceFiction')
    serializer_class = BookSerializer


class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Biography')
    serializer_class = BookSerializer


class PoetryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Poetry')
    serializer_class = BookSerializer


class ClassicsViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Classics')
    serializer_class = BookSerializer
