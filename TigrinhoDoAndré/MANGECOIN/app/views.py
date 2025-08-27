from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TokenView(ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer