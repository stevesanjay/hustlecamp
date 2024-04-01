

from flask import Flask ,request 

app  = Flask(__name__)

@app.route("/")
def home():
    '''
    how to run?
    py app.py
    /?name=steve
    '''

    name = request.values.get("name")

    return f"hello {name}, your name as {len(name)} character"

@app.route("/add")
def add_ui():
    '''
    HOW TO GET THE VALUE FROM THE USER :
    how to run?
    py app.py
    /add?a=5&b=2
    '''

    a = int(request.values.get("a"))
    b = int(request.values.get("b"))
    return str(a + b)

user_dict = { 
	"101": {
	    "name"	:	"steve",
	    "city"	:	"coimbatore",
	    "hobby"	:	"dancing"
	},
	"102": {
	"name"	:	"sam",
	"city"	:	"kkd",
	"hobby"	:	"tennis"
	}

    }

@app.route("/user/<name>/<id>")
def get_user_detail(name,id):
    '''
    HOW TO GET THE VALUE FROM THE USER :
    how to run?
    py app.py
    /user/steve/101     json formate
    '''
    c_user = user_dict[id]
    # return c_user
    result = f"your name:{name} and your are from {c_user['city']}"
    return result


if __name__ == "__main__":
    app.run(debug=True) 




