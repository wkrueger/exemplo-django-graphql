from django.db import models


class WithDate:
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class FileUpload(models.Model, WithDate):
    path = models.FileField(upload_to="media/")


class Profile(models.Model, WithDate):
    PROFILE_CHOICES = [
        ("EMPLOYEE", "Employee"),
        ("STUDENT", "Student"),
        ("SYNDICATE", "Syndicate"),
    ]

    DOCUMENT_TYPE_CHOICES = [("CPF", "CPF"), ("CNPJ", "CNPJ")]

    profileType = models.CharField(max_length=50, choices=PROFILE_CHOICES)
    name = models.CharField(max_length=200)
    documentType = models.CharField(
        max_length=5, choices=DOCUMENT_TYPE_CHOICES, null=True
    )
    document = models.CharField(max_length=50, null=True)


class Tenant(models.Model, WithDate):
    name = models.CharField(max_length=200)
    address = models.TextField(null=True)

    formLogo = models.ForeignKey(
        FileUpload,
        null=True,
        blank=True,
        related_name="tenant_formLogos",
        on_delete=models.DO_NOTHING,
    )
    printLogo = models.ForeignKey(
        FileUpload,
        null=True,
        blank=True,
        related_name="tenant_printLogos",
        on_delete=models.DO_NOTHING,
    )
