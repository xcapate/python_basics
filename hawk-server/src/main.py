from aiohttp import web
import socketio
import random
from flask_api import FlaskAPI
from api_utils import Hawk
from mohawk import Receiver
from flask import request, url_for
import json


#app=web.Application()

app = FlaskAPI(__name__)
hawk = Hawk(app)

@app.route('/')
def index():
    with open('index.html') as f:
        content = f.read()
        return content



@app.route('/api/test',methods=['GET', 'POST'])
def test():
    
    auth_header=request.headers["Authorization"]

    url=request.url

    
    method=request.method

    data=json.dumps(request.data)
    ctype=request.headers['Content-Type']

    try:
        receiver = Receiver(lookup_credentials,auth_header,url,method,content=data,content_type=ctype)
        return {'response':'Welcome to Briefbox'}
    except:
        print("Authentication failed!")
        return {"response":"Authentication failed!"}

    
    


def lookup_credentials(sender_id):
    print("Credentials: " + sender_id)
    senders_data={
                    'id':'company/dxc/hawk.service/contract-room',
                    'key':'pineapplesareprettycool',
                    'algorithm':'sha256'
                }
    return senders_data








#@hawk.client_key_loader
#def get_client_key(client_id):
#    # In a real project you will likely use some storage.
#    if client_id == 'Alice':
#        return 'werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn'
#    else:
#        print("Error auth")
#        raise LookupError()


#@app.route('/')
#@hawk.auth_required
#def index():
    #receiver = Receiver(lookup_credentials,request['headers']['Authorization'],request['url'],request['method'],content=request['content'],content_type=request['headers']['Content-Type'])
#    return 'hello world'




if __name__=='__main__':
    #web.run_app(app,host='0.0.0.0',port='5000')
    app.run(host='0.0.0.0', port=5000)
    #app.run()






