from app.models import FileUpload, Profile, Tenant
import graphene
from graphene_django import DjangoObjectType


class FileUploadType(DjangoObjectType):
    class Meta:
        model = FileUpload
        fields = "__all__"


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


class TenantType(DjangoObjectType):
    class Meta:
        model = Tenant
        fields = "__all__"


class Query(graphene.ObjectType):
    FileUploads = graphene.List(FileUploadType)
    Profiles = graphene.List(ProfileType)
    Tenants = graphene.List(TenantType)

    def resolve_Tenants(_root, _info):
        return Tenant.objects.all()


schema = graphene.Schema(query=Query)
