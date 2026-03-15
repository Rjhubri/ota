from flask import Flask
import webbrowser
from threading import Timer

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return open("templates/index.html", encoding="utf-8").read()


# Page routes
@app.route("/page1")
def page1():
    return open("templates/page1.html", encoding="utf-8").read()

@app.route("/page2")
def page2():
    return open("templates/page2.html", encoding="utf-8").read()

@app.route("/page3")
def page3():
    return open("templates/page3.html", encoding="utf-8").read()

@app.route("/page4")
def page4():
    return open("templates/page4.html", encoding="utf-8").read()

@app.route("/page5")
def page5():
    return open("templates/page5.html", encoding="utf-8").read()

@app.route("/page6")
def page6():
    return open("templates/page6.html", encoding="utf-8").read()

@app.route("/page7")
def page7():
    return open("templates/page7.html", encoding="utf-8").read()

@app.route("/page8")
def page8():
    return open("templates/page8.html", encoding="utf-8").read()

@app.route("/page9")
def page9():
    return open("templates/page9.html", encoding="utf-8").read()

@app.route("/page10")
def page10():
    return open("templates/page10.html", encoding="utf-8").read()


# Auto open browser
def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)