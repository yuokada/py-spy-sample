#!/usr/bin/env  python3.6
from flask import Flask, Response, json

app = Flask(__name__)


@app.route('/name/<name>.json')
def hello_world(name: str) -> object:
    greet = "Hello %s from flask!" % name
    result = {
        "ResultSet": {
            "Result": {
                "Greeting": greet
            }
        }
    }

    response = Response(json.dumps(result))
    response.headers['Content-Type'] = "application/json"
    return response


if __name__ == '__main__':
    app.run(port=8888, debug=False)
