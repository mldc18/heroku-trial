from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return '<h1>It Works!</h1>'

if __name__ == '__main__':
    app.run()