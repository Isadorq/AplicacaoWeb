from .models import *
from .serializers import *
from rest_framework.viewset import ModelViewSet

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer