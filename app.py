from flask import Flask

app = Flask(__name__)

@app.route("/")  # Homepage
def home():
    return "<h1>Welcome to My Website!</h1><p>This is a simple Flask app.</p>"

@app.route("/about")  # About page
def about():
    return "<h1>About Me</h1><p>This page tells you about me!</p>"

if __name__ == "__main__":
    app.run(debug=True)