from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "If you're seeing this message, then this code works."

@app.route("/2016")
def pg2():
    return "This is the second page of the assignment."

@app.route("/1492")
def goodbye():
    return "I have finally completed my work."

if __name__ == "__main__":
    app.run()
