from flask import Flask, render_template
import testdb
app = Flask("app")


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/goofy")
def goofy_ahh_test():
  return render_template("test.html")


