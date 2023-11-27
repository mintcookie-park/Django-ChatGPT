from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'state': True, 'message': '회원가입이 성공적으로 완료되었습니다.', 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response({'state': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(ObtainAuthToken): 
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(username=request.data["username"], password=request.data["password"])
        except User.DoesNotExist:
            user = None

        if user:
            token = Token.objects.get(user=user)
            return Response({'state': True, 'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
        else:
            return Response({'state': False, 'message': '유효하지 않은 인증 정보입니다.'}, status=status.HTTP_401_UNAUTHORIZED)

        response = super().post(request, *args, **kwargs)
        
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.get(user=user)
            print(user, token)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': '유효하지 않은 인증 정보입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    