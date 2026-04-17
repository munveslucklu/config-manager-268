from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "ok", "version": "1.3"}

if __name__ == "__main__":
    app.run(debug=True, port=5723)
