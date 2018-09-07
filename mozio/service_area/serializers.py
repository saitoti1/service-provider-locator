from rest_framework import serializers
from service_area.custom_functions import encrypt_password, check_encrypted_password
from service_area.models import Company, ServiceArea
from service_area.constants import LANGUAGE_CHOICE, CURRENCY_CHOICE
import json
from shapely.geometry import mapping, shape, polygon, point


# noinspection PyAbstractClass
class CreateCompanySerializer(serializers.Serializer):
    """
    This is used to validate when creating a new company instance
    """
    name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICE)
    currency = serializers.ChoiceField(choices=CURRENCY_CHOICE)
    password = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get("password", None)
        if password:
            attrs["password"] = encrypt_password(password)
        return attrs

    def create(self, validated_data):
        return Company.objects.create(**validated_data)


class GetCompanySerializer(serializers.ModelSerializer):
    """
    This is used to serailize a company instance
    """
    class Meta:
        """
        Company Model is assigned to the serializer and certain fields are excluded
        """
        model = Company
        exclude = ('created_at', 'modified_at', 'is_deleted', 'password')


# noinspection PyAbstractClass
class LoginSerializer(serializers.Serializer):
    """
    This is used to serialize login credentials
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        try:
            emp = Company.objects.get(email=attrs.get("email"), is_deleted=False)
        except Company.DoesNotExist:
            raise serializers.ValidationError("Company doesn't exists")
        if not check_encrypted_password(attrs.get("password"), emp.password):
            raise serializers.ValidationError("Company credentials doesn't match")
        return attrs


# noinspection PyAbstractClass
class UpdateCompanySerializer(serializers.Serializer):
    """
    This is used to validate when creating a new company instance
    """
    name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)
    language = serializers.ChoiceField(required=False, choices=LANGUAGE_CHOICE)
    currency = serializers.ChoiceField(required=False, choices=CURRENCY_CHOICE)
    password = serializers.CharField(required=False)

    def validate(self, attrs):
        password = attrs.get("password", None)
        if password:
            attrs["password"] = encrypt_password(password)
        return attrs

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.password = validated_data.get('password', instance.password)
        instance.language = validated_data.get('language', instance.language)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.save()
        return instance


class GetServiceAreaSerializer(serializers.ModelSerializer):
    """
    This is used to serailize a service area instance
    """
    class Meta:
        model = ServiceArea
        exclude = ('created_at', 'modified_at', 'is_deleted')


class SearchServiceAreaSerializer(serializers.ModelSerializer):
    """
    This is used to serailize a searched service area instance
    """
    company = serializers.SerializerMethodField()

    # noinspection PyMethodMayBeStatic
    def get_company(self, service_area):
        """
        This function returns name of the company
        :param service_area:
        :return:
        """
        return service_area.company.name

    class Meta:
        model = ServiceArea
        exclude = ('created_at', 'modified_at', 'is_deleted', 'geo_json')


# noinspection PyAbstractClass
class CreateServiceAreaSerializer(serializers.Serializer):
    """
    This is used to validate when creating a new service area instance
    """
    name = serializers.CharField()
    price = serializers.FloatField()
    geo_json = serializers.JSONField()

    def validate(self, attrs):
        company = self.context.get("company", None)
        if company:
            attrs["company_id"] = company.id
        else:
            raise serializers.ValidationError("Company not provided")
        try:
            s_polygon = shape(json.loads(attrs.get("geo_json", None)).get("geometry", None))
            if isinstance(s_polygon, polygon.Polygon):
                attrs["geo_json"] = mapping(s_polygon)
            else:
                raise TypeError()
        except (TypeError, ValueError, json.JSONDecodeError):
            raise serializers.ValidationError("Invalid geo_json polygon")
        return attrs

    def create(self, validated_data):
        return ServiceArea.objects.create(**validated_data)


# noinspection PyAbstractClass
class UpdateServiceAreaSerializer(serializers.Serializer):
    """
    This is used to validate when creating a new service area instance
    """
    name = serializers.CharField(required=False)
    price = serializers.FloatField(required=False)
    geo_json = serializers.JSONField(required=False)

    def validate(self, attrs):
        if attrs.get('geo_json', None):
            try:
                s_polygon = shape(json.loads(attrs.get("geo_json")).get("geometry", None))
                attrs["geo_json"] = mapping(s_polygon)
            except (TypeError, ValueError, json.JSONDecodeError):
                raise serializers.ValidationError("Invalid geo_json polygon")
        return attrs

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.geo_json = validated_data.get('geo_json', instance.geo_json)
        instance.save()
        return instance


# noinspection PyAbstractClass
class GeoJsonPointSerializer(serializers.Serializer):
    """
    This serializer is used to validate geo_json point
    """
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    point = serializers.SerializerMethodField()

    def get_point(self, attrs):
        try:
            return point.Point(attrs['longitude'], attrs['latitude'])
        except (TypeError, ValueError):
            raise serializers.ValidationError("Invalid geo_json point")
