#!usr/bin/env python
#!coding:utf-8
from flask import Flask,render_template,request
from flask.ext.script import Manager
from livereload import Server
app = Flask(__name__)
manage = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fenlei')
def index1():
    return render_template('fenlei.html')


@manage.command
def dev():
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True,threaded=True)