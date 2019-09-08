from flask import Flask, request

import client

app = Flask(__name__)

final_patent = []

@app.route('/api/patent', methods=['GET', 'POST'])
def patent():
    import random
    random_sorted_args = sorted([random.randint(0, 100) for i in range(12)])
    prepared_random_sorted_args = [{"type": "integer", "value": e, } for e in random_sorted_args]
    final_patent.append(prepared_random_sorted_args)
    print(prepared_random_sorted_args)
    res = client.create_patent(client.MAX1_PRIVATEKEY, prepared_random_sorted_args)
    if res:
        return res
    else:
        return {"Error": "some error occured"}


@app.route('/api/insure', methods=['GET', 'POST'])
def insure():
    res = client.insure(client.MAX1_PRIVATEKEY)
    if res:
        return res
    else:
        return {"Error": "some error occured"}


@app.route('/api/buy', methods=['GET', 'POST'])
def buy():
    try:
        args = final_patent.pop()
    except Exception:
        args = client.args
    res = client.buy_patent(client.MAX2_PRIVATEKEY, args)
    if res:
        return res
    else:
        return {"Error": "some error occured"}


@app.route('/api/win', methods=['GET', 'POST'])
def win():
    import random
    client.args2[0]["value"] = "game"+ str(random.randint(1,1000))
    res = client.send_game_report(client.ORACLE_PRIVATE_KEY, client.args2)
    if res:
        return res
    else:
        return {"Error": "some error occured"}


@app.route('/', methods=['GET', 'POST'])
def add_message():
    content = request.json
    return content


if __name__ == '__main__':
    app.run(debug=True, port=8080)
