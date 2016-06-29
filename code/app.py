from flask import Flask
from redis import Redis
import os
import socket
localIP=socket.gethostbyname(socket.gethostname())
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    showword='Hello Docker ! I have been seen %s times.' % redis.get('hits') + 'From IP:' + socket.gethostbyname(socket.gethostname())
    return '%s' % showword 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
