from flask import Flask

app = Flask(__name__)
        
@app.route("/")
def Body():
    return "Hello DevOps World!"

if __name__ == "__main__":
    Flask.run(app, host = "0.0.0.0", port = 3300)