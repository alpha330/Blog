from rest_framework.decorators import api_view
from rest_framework.response import Response

# views config to send urls.py

@api_view()
def postlist(request):
    return Response("ok")