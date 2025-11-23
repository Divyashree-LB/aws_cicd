from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This Flask app is running on port 6000 and deployed on EC2 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)

