from flask import Flask,jsonify

app=Flask(__name__)


@app.get("/")
def index():
    return "Hello world"

@app.get("/hello")
def hello():
    return jsonify({"Hello":"World"})


app.run(debug=True)

