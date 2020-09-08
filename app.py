from flask import Flask     # import flask class from Flask module

app = Flask(__name__)   # create appllication object

app.config["DEBUG"] = True    # error handling

@app.route("/")
@app.route("/hello")
def hello_world():
    return "Halo Duniaaa"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return f"Hello, {name}", 200
    else:
        return "NoT foUnD", 404

if __name__ == "__main__":
    app.run()
