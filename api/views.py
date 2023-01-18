from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics,permissions

class ListAppUrls(generics.ListAPIView):
    permission_classes=[permissions.BasePermission]

    """
        main page ( list of api urls )
    """
    def get(self, request):
        url = {
                'list Rooms': reverse('list-rooms', request=request),
                'add room ': reverse('new-room', request=request),
            
                
                 }
        # if not request.user.is_anonymous:
        #         user_id=request.user.id 
        #         url['My Account']=reverse('api-account-detail', request=request)
        #         url['My Locations']=reverse('api-locations-list', request=request)
        #         url['My Cart']=reverse('api-mycart-list', request=request)
        #         url['My Mazads']=reverse('api-mymazads-list', request=request)
        #         url['Log Out']=reverse('api-log-out', request=request)
       
               
        # else:
        #     url['Join Us']=reverse('api-sign-up', request=request)
        #     url['Log In']=reverse('api-log-in', request=request)
           
       
        return Response(url)

