# ModelViewSet to serve browsable Django Rest Framework APIs.
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Image, User
from .serializers import UserSerializer, ImageSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class Users(ModelViewSet):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserVerification(APIView):
    permission_classes = []

    def get(self, request, VerStr):
        if Token.objects.filter(key=VerStr).count() == 1:
            tempuser = Token.objects.filter(key=VerStr)[0].user
            tempuser.is_active = True
            tempuser.save()
            site_host = "http://" + str(request.META['HTTP_HOST'])
            return Response({'User_Detail': str(site_host) + '/users/' + str(tempuser.id) + '/',
                             'message': 'Verification successful'})
        else:
            return Response('Please contact support')


class Images(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImagesCompressPath(APIView):
    permission_classes = []

    def get(self, request, pk):
        if Image.objects.filter(id=pk).count() == 1:
            return HttpResponseRedirect(redirect_to=Image.objects.filter(id=pk)[0].full_path)
        else:
            return Response('No Image Found')
