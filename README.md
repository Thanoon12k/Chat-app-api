# Chat-app-api
edit from vscode 



first time doing on ypur local vscode
you should follow this guides to confiure your git setting 
https://gist.github.com/xirixiz/b6b0c6f4917ce17a90e00f9b60566278


👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽
🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵
day 1
git clone <git ssh url> <'folder name'>
cd <'folder name'>
uodate the codes
git add .
git commit -m "message"
git push



day 2
git pull
update the code
git add .
git commit -m "msg"
git push



docker run -p 6379:6379 -d redis:5

import channels.layers
from asgiref.sync import async_to_sync
import asyncio
ch = channels.layers.get_channel_layer()
async_to_sync(ch.send)('test_channel', {'type': 'hello'})
async_to_sync(ch.receive)('test_channel')


loop = asyncio.get_event_loop()