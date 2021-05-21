from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from myapp.models import FeedFile
from .serializers import FeedFileSerializer

# Create your views here.
class FeedFilemodelviewset(ModelViewSet):
    serializer_class=FeedFileSerializer
    queryset=FeedFile.objects.all()
    authentication_classes=[BasicAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated,DjangoModelPermissions]