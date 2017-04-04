from django.contrib.auth.models import User, Group
from rest_framework import views, viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer, GroupSerializer
from api.services import test_service

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TestView(views.APIView):
    def get(self, request):
        return Response(test_service.hello_world())
    def post(self, request):
        return Response(test_service.hello_world())
