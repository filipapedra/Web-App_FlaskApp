from flask import Flask, render_template, request

app = Flask("Test App")

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
