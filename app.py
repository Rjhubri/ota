from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page<int:num>")
def pages(num):
    return render_template(f"page{num}.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
