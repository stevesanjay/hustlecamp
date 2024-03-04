

from flask import Flask, render_template, request
import cph_calculator as ch
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def home_post():
    name = request.values.get("name")
    print(f'name : {name}')
    result = ch.get_detail(name)  # Update function name to match
    return render_template('index.html', myresult=result)

if __name__ == "__main__":
    app.run(debug=True)





