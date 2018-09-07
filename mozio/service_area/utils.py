from service_area.models import Company, AccessToken, ServiceArea
from service_area.serializers import GetCompanySerializer, \
    CreateCompanySerializer, LoginSerializer, UpdateCompanySerializer, \
    GetServiceAreaSerializer, CreateServiceAreaSerializer, \
    UpdateServiceAreaSerializer, GeoJsonPointSerializer, \
    SearchServiceAreaSerializer, shape, json, mapping
from rest_framework import status
import datetime
from service_area.constants import ACCESS_TOKEN_EXPIRY
from service_area.cache import CacheError, CacheService


def generate_access_token(data):
    """
    This method is used to generate access token to be used to access APIs
    :param data:
    :return:
    """
    company = Company.objects.get(email=data.get("email"))
    token = AccessToken.objects.create(
        company=company,
        expiry=datetime.datetime.now() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRY))
    return token.token


def get_companies(query_data=None):
    """
    This method is used to retrieve multiple companies
    :param query_data:
    :return:
    """
    query_params = {
        "is_deleted": False
    }
    if query_data:
        if "company" in query_params and query_data["company"]:
            query_params["id__in"] = query_data["company"]
    response = {}
    companies = Company.objects.filter(**query_params)
    response["success"] = True
    status_code = status.HTTP_204_NO_CONTENT
    if companies:
        serializer_obj = GetCompanySerializer(companies, many=True)
        response["data"] = serializer_obj.data
        response["message"] = "Companies fetched"
        status_code = status.HTTP_200_OK
    else:
        response["data"] = None
        response["message"] = "No Companies found"
    return response, status_code


def create_company(data):
    """
    This method is used to create a company
    :param data:
    :return:
    """
    response = {}
    status_code = status.HTTP_400_BAD_REQUEST
    serializer_obj = CreateCompanySerializer(data=data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        response["data"] = None
        response["message"] = "Company creation successful"
        response["success"] = True
        status_code = status.HTTP_201_CREATED
    else:
        response["data"] = serializer_obj.errors
        response["message"] = "Company creation failed"
        response["success"] = False
    return response, status_code


def update_company(company, data):
    """
    This method is used to update an existing company
    :param company:
    :param data:
    :return:
    """
    response = {}
    status_code = status.HTTP_400_BAD_REQUEST
    serializer_obj = UpdateCompanySerializer(company, data=data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        response["data"] = None
        response["message"] = "Company updation successful"
        response["success"] = True
        status_code = status.HTTP_200_OK
    else:
        response["data"] = serializer_obj.errors
        response["message"] = "Company updation failed"
        response["success"] = False
    return response, status_code


def delete_company(company):
    """
    This method is used to delete an existing company
    :param company:
    :return:
    """
    response = {}
    ServiceArea.objects.filter(is_deleted=False, company=company).delete()
    company.delete()
    status_code = status.HTTP_200_OK
    response["data"] = None
    response["message"] = "Company deletion successful"
    response["success"] = True
    return response, status_code


def get_company(company):
    """
    This method is used to retrieve a single company
    :param company:
    :return:
    """
    response = {}
    serializer_obj = GetCompanySerializer(company)
    response["data"] = serializer_obj.data
    response["message"] = "Companies fetched"
    response["success"] = True
    status_code = status.HTTP_200_OK
    return response, status_code


def login(data):
    """
    This method is used to login for a company and get access token
    :param data:
    :return:
    """
    serializer_obj = LoginSerializer(data=data)
    response = {}
    status_code = status.HTTP_401_UNAUTHORIZED
    if serializer_obj.is_valid():
        token = generate_access_token(serializer_obj.validated_data)
        response["data"] = {"access_token": token}
        response["message"] = "Login Successful"
        response["success"] = True
        status_code = status.HTTP_202_ACCEPTED
    else:
        response["data"] = serializer_obj.errors
        response["message"] = "Login Failed"
        response["success"] = False
    return response, status_code


def create_service_area(company, data):
    """

    :param company:
    :param data:
    :return:
    """
    response = {}
    status_code = status.HTTP_400_BAD_REQUEST
    if data.get('geo_json', None):
        data["geo_json"] = json.dumps(data["geo_json"])
    serializer_obj = CreateServiceAreaSerializer(data=data, context={
        "company": company
    })
    if serializer_obj.is_valid():
        serializer_obj.save()
        response["data"] = None
        response["message"] = "Service Area creation successful"
        response["success"] = True
        status_code = status.HTTP_201_CREATED
    else:
        response["data"] = serializer_obj.errors
        response["message"] = "Service Area creation failed"
        response["success"] = False
    return response, status_code


def update_service_area(service_area_id, data, company):
    """
    This method is used to update service area instance
    :param service_area_id:
    :param data:
    :param company:
    :return:
    """
    response = {}
    status_code = status.HTTP_400_BAD_REQUEST
    try:
        service_area = ServiceArea.objects.get(id=service_area_id, company=company, is_deleted=False)
        serializer_obj = UpdateServiceAreaSerializer(service_area, data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            response["data"] = None
            response["message"] = "Service Area updation successful"
            response["success"] = True
            status_code = status.HTTP_200_OK
        else:
            response["data"] = serializer_obj.errors
            response["message"] = "Service Area updation failed"
            response["success"] = False
    except ServiceArea.DoesNotExist:
        response["data"] = None
        response["message"] = "Service Area updation failed: No such service area"
        response["success"] = False
    except Exception as e:
        print(e)
    return response, status_code


def get_service_area(service_area_id, company):
    """
    This method is used to retrieve a single service area
    :param service_area_id:
    :param company:
    :return:
    """
    response = {}
    status_code = status.HTTP_200_OK
    try:
        service_area = ServiceArea.objects.get(id=service_area_id, is_deleted=False, company=company)
        serializer_obj = GetServiceAreaSerializer(service_area)
        response["data"] = serializer_obj.data
        response["message"] = "Service Area fetched"
        response["success"] = True
    except ServiceArea.DoesNotExist:
        response["data"] = None
        response["message"] = "Service Area not found or you don't have authority over it"
        response["success"] = False
        status_code = status.HTTP_204_NO_CONTENT
    return response, status_code


def get_service_areas(company):
    """
    This method is used to retrieve all service area's of a particular company
    :param company:
    :return:
    """
    response = {}
    service_area = ServiceArea.objects.filter(company=company, is_deleted=False)
    if service_area:
        serializer_obj = GetServiceAreaSerializer(service_area, many=True)
        response["data"] = serializer_obj.data
        response["message"] = "Service Area fetched"
        response["success"] = True
        status_code = status.HTTP_200_OK
    else:
        response["data"] = None
        response["message"] = "No Service Areas found"
        response["success"] = False
        status_code = status.HTTP_204_NO_CONTENT
    return response, status_code


def delete_serializer(service_area_id, company):
    """
    This method is used to delete an existing service area
    :param service_area_id:
    :param company:
    :return:
    """
    response = {}
    status_code = status.HTTP_200_OK
    try:
        ServiceArea.objects.get(is_deleted=False, id=service_area_id, company=company).delete()
        response["data"] = None
        response["message"] = "Service Area deletion successful"
        response["success"] = True
    except ServiceArea.DoesNotExist:
        response["data"] = None
        response["message"] = "Service Area not found or you don't have authority over it"
        response["success"] = False
    return response, status_code


def search_serializers(data):
    """
    This method searches all active service areas and returns those which
    :param data:
    :return:
    """
    response = {}
    status_code = status.HTTP_200_OK
    service_areas = ServiceArea.objects.filter(is_deleted=False)
    matching_service_area = []
    serializer_obj = GeoJsonPointSerializer(data=data)
    response_data = {}
    if serializer_obj.is_valid():
        point = serializer_obj.data["point"]
        response_data = CacheService.get(json.dumps(mapping(point)))
        if not response_data:
            for service_area in service_areas:
                polygon = shape(service_area.geo_json)
                if polygon.contains(point):
                    matching_service_area.append(service_area)
            response_data = SearchServiceAreaSerializer(
                        matching_service_area, many=True).data
            try:
                CacheService.set(json.dumps(
                    mapping(point)),
                    response_data)
            except CacheError:
                pass
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        response["data"] = serializer_obj.errors
        response["message"] = "Search for service area failed"
        response["success"] = False
        return response, status_code
    response["data"] = response_data
    response["message"] = "Search for service area successful"
    response["success"] = True
    return response, status_code
