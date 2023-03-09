
from utilsapp.models import Notification,ProductFollowers
from usersapp.models import MyUser  


def send_notify(sender=None,title=None,medicine=None,url=None,status=None):
        recipient=None
        if title=='new_user':
                    body=f'new user registered'
                    recipient=MyUser.objects.filter(mobile=100)
        
        recipient=recipient.distinct()
        if not recipient:
            return ('no recption provide')
        
        for r in recipient:
            notify=Notification.objects.filter(recipient=r,title=title_english,body=body_english)
            if not notify:
                notify=Notification.objects.create(recipient=r,medicine=medicine,title=title,body=body,url=url )
        return notify