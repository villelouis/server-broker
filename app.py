from flask import Flask,request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/patent', methods=['GET', 'POST'])
def add_message():
    content = request.json
    return content


if __name__ == '__main__':
    app.run()
