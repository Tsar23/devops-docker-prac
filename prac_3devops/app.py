from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "DevOps Practical 3: Web Service is running successfully. Developed by Volodymyr Tsar, group KN-32sp."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)