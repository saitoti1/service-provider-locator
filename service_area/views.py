from rest_framework.views import APIView
from rest_framework.response import Response
from service_area import utils
from service_area import permissions


class CompanySRUD(APIView):
    """
    This APIVIew has single retrieve, update and delete methods
    """
    permission_classes = (permissions.CompanyAccessPermission,)

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        """
        description: This API is used to retrieve single company instance
        parameters:
            - name: email
              description: Email id of company
              required: false
            - name: password
              description: Password of company
              required: false
            - name: phone_number
              required: false
            - name: language
              required: false
            - name: currency
              required: false
            - name: name
              required: false
        """
        (response, status_code) = utils.get_company(request.user)
        return Response(response, status=status_code)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        """
        description: This API is used to update a company instance
        """
        (response, status_code) = utils.update_company(request.user, request.data)
        return Response(response, status=status_code)

    # noinspection PyMethodMayBeStatic
    def delete(self, request):
        """
        description: This API is used to delete a company instance
        """
        (response, status_code) = utils.delete_company(request.user)
        return Response(response, status=status_code)


class CompanyCMRL(APIView):
    """
    This APIView has search, create and multiple instance retrive methods
    """

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def get(self, request):
        """
        description: This API is used to retieve multiple company instances
        """
        (response, status_code) = utils.get_companies()
        return Response(response, status=status_code)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        """
        description: This API is used to create a new service area instance
        parameters:
            - name: price
              description: Price of service area
              required: true
            - name: geo_json
              required: true
            - name: name
              required: true
        """
        (response, status_code) = utils.create_company(request.data)
        return Response(response, status=status_code)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        """
        description: This API is used to login
        parameters:
            - name: email
              description: Email id of company
              required: true
            - name: password
              description: Password of company
              required: true
        """
        (response, status_code) = utils.login(request.data)
        return Response(response, status=status_code)


class ServiceAreaCMR(APIView):
    """
    This APIView has create and multiple instance retrive methods
    """
    permission_classes = (permissions.CompanyAccessPermission,)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        """
        description: This API is used to create a new company instance
        parameters:
            - name: email
              description: Email id of company
              required: true
            - name: password
              description: Password of company
              required: true
            - name: phone_number
              required: true
            - name: language
              required: true
            - name: currency
              required: true
            - name: name
              required: true
        """
        (response, status_code) = utils.create_service_area(request.user, request.data)
        return Response(response, status=status_code)

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        """
        description: This API is used to retieve multiple service area instances of a company
        """
        (response, status_code) = utils.get_service_areas(request.user)
        return Response(response, status=status_code)


class ServiceAreaSRUD(APIView):
    """
    This APIVIew has single retrieve, update and delete methods
    """
    permission_classes = (permissions.CompanyAccessPermission,)

    # noinspection PyMethodMayBeStatic
    def get(self, request, service_area_id):
        """
        description: This API is used to retrieve single service area instance
        """
        (response, status_code) = utils.get_service_area(service_area_id, request.user)
        return Response(response, status=status_code)

    # noinspection PyMethodMayBeStatic
    def put(self, request, service_area_id):
        """
        description: This API is used to update a service area instance
        """
        (response, status_code) = utils.update_service_area(service_area_id, request.data, request.user)
        return Response(response, status=status_code)

    # noinspection PyMethodMayBeStatic
    def delete(self, request, service_area_id):
        """
        description: This API is used to delete a service instance
        """
        (response, status_code) = utils.delete_serializer(service_area_id, request.user)
        return Response(response, status=status_code)


class SearchServiceArea(APIView):
    """
    This APIView is used to search a point in active service areas
    """

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        """
        description: This API is used to search for service areas at a point
        :param request:
        :return:
        """
        (response, status_code) = utils.search_serializers(request.data)
        return Response(response, status=status_code)
