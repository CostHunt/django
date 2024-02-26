from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.contrib import messages
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
import pyrebase
from django.conf import settings

config = {
    "apiKey": "AIzaSyBBft9zuyWSPT6VabyDCb3hbN83PWK9Db8",
    "authDomain": "test-22991.firebaseapp.com",
    'projectId': "test-22991",
    "storageBucket": "test-22991.appspot.com",
    "messagingSenderId": "169698943184",
    "appId": "1:169698943184:web:5fc79b43ef521964dd3ed5",
    "measurementId": "G-9NJQ2Q5327",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')

        if file:
            file_name = file.name
            file_path = f"media/{file_name}"
            storage_path = f"files/{file_name}"

            # Save file to default storage
            file_save = default_storage.save(file_name, file)

            try:
                # Upload file to Firebase Storage
                storage.child(storage_path).put(file_path)
                response_data = {"File uploaded to Firebase Storage": storage_path}
                status_code = status.HTTP_202_ACCEPTED
            except Exception as e:
                response_data = {"Error uploading file to Firebase Storage": str(e)}
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            finally:
                # Delete file from default storage
                delete = default_storage.delete(file_name)
                response_data["File deleted from"] = file_path

            return Response(response_data, status=status_code)

        return Response({"error": "File not provided"}, status=status.HTTP_400_BAD_REQUEST)


class FileURLAPIView(APIView):
    def get(self, request, file_name):
        storage_path = f"files/{file_name}"

        try:
            file_url = storage.child(storage_path).get_url(None)
            return Response({'file_url': file_url, 'file_name': file_name}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), 'file_name': file_name}, status=status.HTTP_404_NOT_FOUND)
# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})