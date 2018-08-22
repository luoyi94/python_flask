from code23_blue import app


@app.route("/user")
def user():
    return "user"