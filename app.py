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
        max_length = 8
        row = [words_list for _ in range(8)]
        grid = [row for x in row]
        for i in grid:
            for j in i:
                grid.append([])
            for j in words_list:
                grid[-1].append(0)
                print(grid)
                     
    return render_template("create.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
