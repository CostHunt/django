from rest_framework import serializers
from .models import  User
from .models import  Message
from .models import  AttachedFile
from .models import  Role
from .models import  Appartenir
from .models import  Attacher
from .models import  Contenir

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','name','image','email','password','createdAt','updatedAt')
        extra_kwargs = {
            'password': { 'write_only': True}
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id_message','id_groupe', 'username', 'contenu', 'date_envoie', 'createdAt', 'updatedAt')

class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = ('id_file','nomfichier', 'path', 'createdAt', 'updatedAt')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('code_role','libelle_role', 'createdAt', 'updatedAt')

class AppartenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartenir
        fields = ('id_groupe','username','code_role', 'createdAt', 'updatedAt')

class AttacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attacher
        fields = ('id_message','id_file', 'createdAt', 'updatedAt')

class ContenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenir
        fields = ('id_post','id_file', 'createdAt', 'updatedAt')
