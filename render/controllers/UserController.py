import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from render.models import Role, User
from render.serializers import UserSerializer
from rest_framework import status
from render.controllers.Authentification import validateToken
@api_view(['GET','POST'])
def GetUser(request):
    if request.method == 'GET':
        if validateToken(request):
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'NOT AUTHORIZED'},status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT', 'DELETE'])
def UpdateDeleteUser(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if validateToken(request):
            request_data = json.loads(request.body)
            serializer = UserSerializer(user, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'NOT AUTHORIZED'},status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'DELETE':
        if validateToken(request):
            user.delete()
            return Response({'error': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'NOT AUTHORIZED'},status=status.HTTP_401_UNAUTHORIZED)