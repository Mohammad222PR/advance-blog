from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60)
def test(request):
    response = requests.get('https://a9f6156f-b274-4522-88af-a2df25158396.mock.pstmn.io/test/delay/5')
    return JsonResponse(response.json())