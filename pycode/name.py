from flask import Flask, request, render_template
app = Flask(__name__)

# @app.route("/")
# def name():
#      name = request.values.get("name")
#      return f"{name[::-1]}"



# @app.route("/rname",methods =["post"])
# def rname():
#     name = request.values.get("name")
#     # result = f"{name[::-1]}"
#     result = f"hello {name}, and your name has {len(name)} characters" 

#     return render_template(
#         'index.html',
#         my_result = result
#         )

# if __name__ == "__main__":
#     app.run(
#         debug = True
#     )


@app.route("/submitname")
def r_name():
    name = request.values.get("name")
    result = f"you Name{name}, your Name has{len(name)}character"
    