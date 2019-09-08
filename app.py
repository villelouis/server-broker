from flask import Flask,request
import client

app = Flask(__name__)


@app.route('/')
def hello_world():
    import random
    random_sorted_args = sorted([random.randint(1, 100) for i in range(12)])
    prepared_random_sorted_args = [{"type": "integer", "value": e,} for e in random_sorted_args]
    print(prepared_random_sorted_args)
    client.create_patent(client.MAX1_PRIVATEKEY, prepared_random_sorted_args)
    return 'Hello World!'

@app.route('/api/patent', methods=['GET', 'POST'])
def add_message():
    content = request.json
    return content


if __name__ == '__main__':
    app.run(debug=True, port=8080)
