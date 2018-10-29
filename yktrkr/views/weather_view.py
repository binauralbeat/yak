from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
import operator
from django.db.models import Q
import requests
import json

# this just loads the weather.html template
def weather (request):
    '''
    search bar result
    '''
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=87bb544805fd6c3c51684b576b7d7c84')
    print(response)
    weather_data = response.json()
    print(weather_data)
    query = request.GET.get('q')
    if query == None:
        q_str = 'nashville'
    elif query != None:
        q_str = str(query)
        print (q_str)

    return render(request, 'weather.html', {'q_str': q_str})