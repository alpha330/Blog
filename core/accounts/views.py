from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.cache import cache
import requests
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60 * 15)
def test(request):
    Response = requests.get("https://a89d010f-1b29-4211-b34b-0ce6c63ed80e.mock.pstmn.io/test/delay/5")
    return JsonResponse(Response.json())