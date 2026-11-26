from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)


@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    data = dbHandler.listExtension()
    return render_template("/index.html", content=data)


@app.route("/add.html", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        dbHandler.insertContact(email, name)
        return render_template("/add.html", is_done=True)
    else:
        return render_template("/add.html")


@app.route("/about.html", methods=["GET"])
def about():
    ##  data = dbHandler.listExtension()
    return render_template("/about.html")


@app.route("/SSA", methods=["GET"])
def SSA_page():
    data = dbHandler.listSSA()
    return render_template("/index.html", content=data)


@app.route("/SG", methods=["GET"])
def SG_page():
    data = dbHandler.listSG()
    return render_template("/index.html", content=data)


@app.route("/SF", methods=["GET"])
def SF_page():
    data = dbHandler.listSF()
    return render_template("/index.html", content=data)


@app.route("/STT", methods=["GET"])
def STT_page():
    data = dbHandler.listTT()
    return render_template("/index.html", content=data)


@app.route("/SS", methods=["GET"])
def SS_page():
    data = dbHandler.listSS()
    return render_template("/index.html", content=data)


@app.route("/SI", methods=["GET"])
def SI_page():
    data = dbHandler.listSI()
    return render_template("/index.html", content=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
