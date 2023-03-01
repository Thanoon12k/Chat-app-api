import pyrebase
import base64

import random
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



def SendMessage(id,sender,sender_name,room_id,text,sendtime):
    
    # image=get_image_data('media\hash.jpg')

    data = {
        'id': 5,
        'sender': sender,
        'sender_name':sender_name,
        'room_id':room_id,
        'text': text, 
        'attachment': None,
        'DateTime':sendtime,
    }
   
    send = database.child('messages').push(data)
    return 'message_sended_ok'

def save_image(image_data):
    image_data = base64.b64decode(image_data)
    with open('media/my.jpg', 'wb') as f:
            f.write(image_data)
def get_image_data(image_path):
    
    with open(image_path, 'rb') as f:
        image_data = f.read()
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    return encoded_image
    


















def GetName():
    name = database.child('Rooms').get().val()
    # print(f'name : {name}')
   
    return name

def GetRooms(path):
    rooms = database.child(path).get().val()
   
    return rooms
