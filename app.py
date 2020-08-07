from flask import Flask, redirect, url_for, render_template, request
from flask_restful import Resource, Api, reqparse
# from flask_jwt import JWT, jwt_required

# from security import authenticate, identity
# from resources.user import UserRegister  
from resources.task import Task



app = Flask(__name__)
api = Api(app)


@app.route("/")
def home():
  return render_template("index.html")

@app.route("/search", methods=["POST", "GET"])
def search():
  if request.method == "POST":
      key_word = request.form["key_word"]
      return redirect(url_for("search_for_ref", word=key_word))
  else:
      return render_template("search.html")

@app.route("/<word>")
def search_for_ref(word):
  return "this came from the search-for-ref route function in the app it will return the rows from the database"





# app.secret_key = 'jose'

# jwt = JWT(app, authenticate, identity)



api.add_resource(Task, '/task/<string:task>')



# api.add_resource(Itemlist, '/items')
# api.add_resource(UserRegister, '/register')

# debug=True will allow the source of the API to be updated and synced without restarting the API
if __name__=='__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')