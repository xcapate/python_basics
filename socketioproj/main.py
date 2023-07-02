from aiohttp import web
import socketio
import random

#crea un server asincrono
sio= socketio.AsyncServer()
#crea una nueva aplicacion web
app=web.Application()
#liga la pliacion al servidor socketio
sio.attach(app)

async def index(request):
    with open('index.html') as f:
        content = f.read()
        #lee y parsea el html(content), finalmente lo devuelve como respuesta tipo html
        return web.Response(text=content, content_type='text/html')

@sio.on('message')
async def print_message(sid,message):
    print('Socket Id: ',sid)
    print("\r\n" + message)
    random_answers=["whats up!","Hey there!","Dude Hi!","Who's there?"]
    answer=random.choice(random_answers)
    await sio.emit('message', answer)

app.router.add_get('/',index)

if __name__=='__main__':
    web.run_app(app)