# from django.core.serializers import json
import json
from django.shortcuts import HttpResponse


def hello_world(request: object, name: str) -> object:
    greet = "Hello %s from flask!" % name
    result = {
        "ResultSet": {
            "Result": {
                "Greeting": greet
            }
        }
    }

    response = HttpResponse(json.dumps(result), status=200)
    response['Content-Type'] = 'application/json'
    return response
