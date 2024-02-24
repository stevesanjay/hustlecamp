

# from flask import Flask
# app = Flask(__name__)

# user_dict ={
#     "place"
# }


# return f"city{city[::-1]}"

# @app.route("/")
# def city():
    
from flask import Flask ,request , render_template

app =  Flask(__name__)

# @app.route("/")

# def add():
#     a = int(request.values.get("a"))
#     b = int(request.values.get("b"))
#     return a+b 

@app.route("/")
def add():

    a = int(request.values.get("a"))
    b = int(request.values.get("b"))
    result = a+b

    return render_template(
        'index.html',
        myresult = str(result)
        )
    
if __name__ == "__main__":
    app.run(
        debug = True
    )

