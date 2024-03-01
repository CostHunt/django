from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=32,)
    prenoms = models.CharField(max_length=32,)
    password = models.CharField(max_length=250,)
    matricule = models.CharField(max_length=32,)
    email = models.CharField(max_length=50,)
    image = models.CharField(max_length=32,)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)


class Groupe(models.Model):
    id_groupe =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_groupe = models.CharField(max_length=32, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id_comment =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    id_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    contenu = models.CharField(max_length=32, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    id_post =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=32, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    id_message =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.CharField(max_length=32, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class AttachedFile(models.Model):
    id_file =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomfichier = models.CharField(max_length=32, null=True)
    path = models.CharField(max_length=32, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    code_role =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    libelle_role = models.CharField(max_length=32, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Appartenir(models.Model):
    id_appartenir =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    code_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Attacher(models.Model):
    id_attacher =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_message = models.ForeignKey(Message, on_delete=models.CASCADE)
    id_file = models.ForeignKey(AttachedFile, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Contenir(models.Model):
    id_contenir =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_file = models.ForeignKey(AttachedFile, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

