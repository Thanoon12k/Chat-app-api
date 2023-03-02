from rest_framework.response import Response
from django.http import HttpResponse

def Root(request):
    # resp=SetRoom()
    # name=GetName()
    # rooms=GetRooms('Root')
    
    return HttpResponse('resp' )