"""app apis."""
from rest_framework.views import APIView
from rest_framework.response import Response

from app import services


class CarSearchAPI(APIView):

    def get(self, request):
        keyword = request.query_params.get('k', '')

        retdata = {'result': services.car_search(keyword)}
        return Response(retdata)


class HttpCodeSearchAPI(APIView):

    def get(self, request):
        keyword = request.query_params.get('k', '')

        retdata = {'result': services.http_code_search(keyword)}
        return Response(retdata)



class ShortUrlCodeAPI(APIView):

    def get(self, request):
        url = request.query_params.get('url', '')

        retdata = {'result': services.get_short_url_code(url)}
        return Response(retdata)
