from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .permissions import IsUserOrReadOnly
from .serializers import UserSerializer

User = get_user_model();


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly)