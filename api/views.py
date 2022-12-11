from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import CountrySerializer
# Create your views here.
from .models import Country


# class CountryListView(ListAPIView):
#     queryset=Country.objects.all()
#     serializer_class= CountrySerializer

class CountryListView(ListCreateAPIView):
    queryset=Country.objects.all()
    serializer_class= CountrySerializer

# class CountryListView(RetrieveAPIView):
#     queryset=Country.objects.all()
#     serializer_class= CountrySerializer

# class CountryListView(RetrieveUpdateAPIView):
#     queryset=Country.objects.all()
#     serializer_class= CountrySerializer

class CountryDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Country.objects.all()
    serializer_class= CountrySerializer