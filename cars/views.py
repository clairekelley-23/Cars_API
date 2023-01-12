from rest_framework.decorators import api_View
from rest_framework.response import Reponse

@api_View(['GET'])
def cars_list(request):


    return Reponse('ok')