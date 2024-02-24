from flask import Flask ,request , render_template

app =  Flask(__name__)

@app.route("/")

def home():

    name = request.values.get("name", "steve")
    result = f"hello {name}, and your name has {len(name)} characters"
    
    return result

@app.route("/submitname")
def input_from_ui():

    name = request.values.get("name", "steve")
    result = f"hello {name}, and your name has {len(name)} characters"
    
    return render_template(
        'index.html',
        my_result =result
        )



@app.route("/add")
def app_id():
    a = int(request.values.get("a"))
    b = int(request.values.get("b"))

    return str(a+b)


 

user_dict = { 
    "130" : {
        "name" : "akilan",
        "hobby" : "painting",
        "place" : "ukkadam"
        },
    "131" : {
        "name" : "muthu",
        "hobby": "dance",
        "place": "malumichampatti"
        },
    "132" : {
        "name" : "manoj",
        "hobby" : "singing",
        "place" : "nava india"
        },
    "133" : {
        "name" : "joshua",
        "hobby": "watching tv",
        "place": "kinathukadavu"
        }
}
@app.route("/user/<name>/<id>")
def get_user_details(name, id ):

    c_user = user_dict[id]
    #result = f"Name : {name}, and you from {c_user['place']}"
    
    result = {
        "user_details" : c_user 
    }
    return render_template(
        'index.html',
        my_result =result
        )

     
if __name__ == "__main__":
    app.run(
        debug = True
    )