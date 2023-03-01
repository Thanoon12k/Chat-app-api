from rest_framework.response import Response
from django.http import HttpResponse

from .firebase import *
def Root(request):
    # resp=SetRoom()
    # name=GetName()
    # rooms=GetRooms('Root')
    
    return HttpResponse('resp' )