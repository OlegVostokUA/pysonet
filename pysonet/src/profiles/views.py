from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from .models import UserNet
from .serializers import GetUserNetSerializer


class GetUserNetView(RetrieveAPIView):
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer


"""
class UserNetPublicView(ModelViewSet):
   
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]

"""