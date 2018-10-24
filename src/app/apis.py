"""app apis."""
from rest_framework.views import APIView
from rest_framework.response import Response

from app import services


class CarSearchAPI(APIView):

    def get(self, request):
        keyword = request.query_params.get('k', '')

        retdata = {'result': services.car_search(keyword)}
        return Response(retdata)
