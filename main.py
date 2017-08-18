from flask import Flask
from flask import render_template

app = Flask(__name__)
app.secret_key = 'fsdfhl oip.ljhklh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


from message import main as message_route
from user import main as user_route
from bbs import main as bbs_route
from api import main as api_route

app.register_blueprint(message_route)
app.register_blueprint(user_route)
app.register_blueprint(bbs_route, url_prefix='/bbs')
app.register_blueprint(api_route,
                       url_prefix='/api')


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')


@app.errorhandler(410)
def error404(e):
    return render_template('410.html')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=True,
    )
    app.run(**config)
