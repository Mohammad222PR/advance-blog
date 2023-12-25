from django.shortcuts import render
from django.http import JsonResponse
from .tasks import test
import requests
from django.core.cache import cache
# Create your views here.


def test(request):
    if cache.get('test_api_delay') is None:
        response = requests.get('https://a9f6156f-b274-4522-88af-a2df25158396.mock.pstmn.io/test/delay/5')
        cache.set("test_api_delay", response.json())
    return JsonResponse(cache.get("test_api_delay"))