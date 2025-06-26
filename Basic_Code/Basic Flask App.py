from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi Guys This is Gowtham G.s Patil!"

if __name__ == '__main__':
    app.run(debug=True)
