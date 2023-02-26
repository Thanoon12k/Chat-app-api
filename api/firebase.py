import pyrebase
import requests
import base64

config = {
    'apiKey': "AIzaSyC5-uBI417-LL6tVvQhLXOQ7pXSiE2SeN8",
    'authDomain': "chatapp-6fbfd.firebaseapp.com",
    'projectId': "chatapp-6fbfd",
    'storageBucket': "chatapp-6fbfd.appspot.com",
    'messagingSenderId': "353002107934",
    'appId': "1:353002107934:web:3145c44123e49547adea0f",
    "databaseURL": "https://chatapp-6fbfd-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def SetRoom():
    import random
    
    n = random.randint(1, 100)
    image_path = 'C:\\Users\\mohsal\\Desktop\\app\\freelancer\\chatapp_backend\\api\\media\\hash.jpg'
    # with open(image_path, 'rb') as f:
    #     image_data = f.read()
    # encoded_image = base64.b64encode(image_data).decode('utf-8')

    data = {
        'id': n,
        'text': 'hi iam the last', 
        'sender': 1,
        'image': 'encoded_image'
    }
   
    send = database.child('messages').push(data)
    messages_resp=database.child('messages').get().val().keys()
    last_id=list(messages_resp)[-1]
    last_message = database.child('messages').child(last_id).get().val().values()
    
    return list(last_message)
    

    
def GetName():
    name = database.child('Rooms').get().val()
    # print(f'name : {name}')
   
    return name

def GetRooms(path):
    rooms = database.child(path).get().val()
   
    return rooms
