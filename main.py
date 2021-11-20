
from flask import Flask

from wsgiref import simple_server

from flask import Flask, session, request, Response, jsonify



import atexit
import uuid
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running"

port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    #app.run(host="0.0.0.0",port=5000)
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host, port=port, app=app)
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    #print("Serving on %s %d" % (host, port))
    httpd.serve_forever()