from django.urls import path
from .controllers.Authentification import Login, Decode, Signup
from . import views
from .views import FileUploadAPIView, FileURLAPIView
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', Login, name='get-token'),
    path('verify/', Decode, name='verify-token'),
    path('register/', Signup, name='sing up'),
    path('upload/', FileUploadAPIView.as_view(), name='file-upload-api'),
    path('file/<file_name>/', FileURLAPIView.as_view(), name='get_file_url'),
]