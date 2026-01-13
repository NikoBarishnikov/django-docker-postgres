from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



def index(request):
    return render(request, 'person/index.html')

@method_decorator(csrf_exempt, name='dispatch')
class PersonListCreateAPIView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

@method_decorator(csrf_exempt, name='dispatch')
class PersonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


