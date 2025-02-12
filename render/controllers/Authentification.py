from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import jwt
from datetime import datetime, timedelta
from render.models import User
from render.serializers import UserSerializer
from mysite.settings import SECRET_KEY

@api_view(['GET', 'POST'])
def Login(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        username = request_data.get('username')
        password = request_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid username',}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.check_password(password):
            expiration_time = datetime.utcnow() + timedelta(seconds=20)
            token = jwt.encode(
                {
                    'username': user.username,
                    'matricule':user.matricule,
                    'nom': user.nom,
                    'prenoms':user.prenoms,
                    'email': user.email,
                    'exp': expiration_time,

                },
                SECRET_KEY,
                algorithm='HS256' 
                )
            return Response({'token': token}, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Invalid password',}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Decode (request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        token = request_data.get('token')
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return Response({'user': decoded_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def Signup (request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        serializerUser = UserSerializer(data=request_data)
        if serializerUser.is_valid():
            user = serializerUser.save()
            expiration_time = datetime.utcnow() + timedelta(seconds=20)
            token = jwt.encode(
                {
                    'username': user.username,
                    'nom': user.nom,
                    'matricule':user.matricule,
                    'prenoms':user.prenoms,
                    'email': user.email,
                    'exp': expiration_time,
                },
                SECRET_KEY,
                algorithm='HS256' 
                )
            response_data = UserSerializer(user).data
            response_data["token"] = token
            return Response(response_data, status=status.HTTP_201_CREATED)
        return JsonResponse({'errors': serializerUser.errors}, status=status.HTTP_400_BAD_REQUEST)

def validateToken(request):
    token_key_header = request.headers.get('X-access-token')
    if token_key_header:
        try:
            jwt.decode(token_key_header, SECRET_KEY, algorithms=['HS256'])
            return True
        except:
            return False
    else:
        return False