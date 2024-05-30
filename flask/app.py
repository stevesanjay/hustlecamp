

'''
Created on 

@author: Raja CSP Raman

source:
    https://chatgpt.com/share/7c92b746-9835-4d51-9359-0b59b6fbc682
    https://flask-limiter.readthedocs.io/en/stable/  
'''

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# initialize flask limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

# Attach the limiter to the app
# limiter.init_app(app)

@app.route("/slow")
@limiter.limit("3 per day")
def index():
    return "hello world"


@app.route("/medium")
@limiter.limit("6 per day", override_defaults=False)
def medium():
    return "hello steve"




@app.errorhandler(429)
def ratelimit_handler(e):
    return "you exceeds the limit",429


if __name__ == '__main__':
    app.run(debug=True)