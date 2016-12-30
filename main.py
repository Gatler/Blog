from flask import Flask
from flask import render_template

app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = 'fsdfhloip.ljhklh'
# 这一行是套路
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# 引入、注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀

from weibo import main as weibo_routes
from user import main as user_routes
from blog import main as blog_routes
from api import main as api_routes

app.register_blueprint(weibo_routes)
app.register_blueprint(user_routes)
app.register_blueprint(blog_routes, url_prefix='/blog')
app.register_blueprint(api_routes,
                       url_prefix='/api')


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')


@app.errorhandler(410)
def error404(e):
    return render_template('410.html')


# 运行代码
if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=True,
    )
    app.run(**config)
