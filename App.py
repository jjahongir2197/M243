from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""

    if request.method == "POST":
        username = request.form["username"]

        if username == "admin":
            msg = "Admin panelga xush kelibsiz"
        else:
            msg = "User sahifasi"

    return render_template("index55.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
