from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
# Create your views here.

def test(request):
    Response = requests.get("https://a89d010f-1b29-4211-b34b-0ce6c63ed80e.mock.pstmn.io/test/delay/5")
    return JsonResponse(Response.json())