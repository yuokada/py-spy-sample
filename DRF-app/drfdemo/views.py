from rest_framework.generics import GenericAPIView
# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, views


class DemoAPI(viewsets.GenericViewSet):

    def get(self, request, name, format=None):
        greet = "Hello %s from flask!" % name
        result = {
            "ResultSet": {
                "Result": {
                    "Greeting": greet
                }
            }
        }
        return Response(data=result)

class Demo2API(views.APIView):

    def get(self, request, name, format=None):
        greet = "Hello %s from flask!" % name
        result = {
            "ResultSet": {
                "Result": {
                    "Greeting": greet
                }
            }
        }
        print("Format is " +  str(format))
        return Response(data=result)
