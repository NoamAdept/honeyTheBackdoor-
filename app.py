from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Valid login credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "securepassword"

# The flag file
FLAG_FILE = "flag.txt"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Normal user authentication
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session["authenticated"] = True
            return redirect(url_for("dashboard"))

        return render_template("index.html", error="Invalid username or password")

    return render_template("index.html", error=None)


@app.route("/dashboard")
def dashboard():
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    # Read and display the flag
    with open(FLAG_FILE, "r") as f:
        flag = f.read().strip()

    return render_template("dashboard.html", flag=flag)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
