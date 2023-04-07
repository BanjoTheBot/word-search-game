from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("name")
        words = request.form.get("words")
        words_list = words.split()
        print (words_list)
    return render_template("create.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
