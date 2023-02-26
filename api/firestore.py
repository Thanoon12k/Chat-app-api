import pyrebase
import requests
config={
     'apiKey': "AIzaSyC5-uBI417-LL6tVvQhLXOQ7pXSiE2SeN8",
  'authDomain': "chatapp-6fbfd.firebaseapp.com",
  'projectId': "chatapp-6fbfd",
  'storageBucket': "chatapp-6fbfd.appspot.com",
  'messagingSenderId': "353002107934",
  'appId': "1:353002107934:web:3145c44123e49547adea0f",
  "databaseURL": "https://chatapp-6fbfd-default-rtdb.firebaseio.com",
   
 
}
firebase=pyrebase.initialize_app(config)    
authe = firebase.auth()
database=firebase.database()

def GetName():
    name = database.child('Rooms').get().val()
    # print(f'name : {name}')
   
    return name

def GetRooms(path):
    rooms = database.child(path).get().val()
   
    return rooms

def SetRoom():
    import random
    url='https://chatapp-6fbfd-default-rtdb.firebaseio.com/'
    data = {'name': 'John', 'age': 30}
    response = requests.get(url)
    n=random.randint(1, 100)
    # print(f' n : {n} ')
    image='media/hash.jpg'
    data={ 
     'id': n,
      'text': 'hi iam wanted text', 
      'sender': 1, 
      },
    message = database.child('messages').push(data)
    resp1 = list(database.child('messages').get().val().keys())
    child_message='-NPBnZEBM8y9ZPocME43'
    resp2 = list(database.child('messages').child(child_message).get().val())
   
    return resp2

