from flask import Flask,redirect,url_for,render_template,request,session
import os,socket,time,json
import config
from flask import current_app

app = Flask(__name__)
############加载db配置
app.config.from_object(config)
##############session加盐
app.config['SECRET_KEY'] = '~\xc8\xc6\xe0\xf3,\x98O\xa8z4\xfb=\rNd'

#db=SQLAlchemy(app)


@app.route('/',methods=['GET'])
def hello_world():
    return redirect('index.html')

@app.route('/index.html',methods=['GET'])
def index_html():
    return render_template('index.html')

@app.route('/<fileurl>.html')
def viewhtml(fileurl):
    return render_template(fileurl + '.html')


if __name__ == '__main__':
    app.run(debug=True)
