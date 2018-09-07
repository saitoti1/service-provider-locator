from django.db import models
import uuid
from django.contrib.postgres.fields import JSONField
from service_area.constants import LANGUAGE_CHOICE, CURRENCY_CHOICE

# Create your models here.


class ModelBase(models.Model):
    """
    This is the base models which holds common fields in all the models
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class Company(ModelBase):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICE)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "company"


class ServiceArea(ModelBase):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    geo_json = JSONField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "service_area"


class AccessToken(ModelBase):
    """
    This is the model which stores access tokens which is used by employee to gain access to APIs
    """

    token = models.UUIDField(default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    expiry = models.DateTimeField()

    class Meta:
        db_table = "access_token"
