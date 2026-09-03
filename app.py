from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return return "Day 16 CI/CD Deployment SUCCESS!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
