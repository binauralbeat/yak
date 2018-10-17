from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
import operator
from django.db.models import Q
import requests
import json

# this is all abandoned for iframe at the moment
def boat_ramps (request):
    '''
    function that locates and displays the locations of nearby
    boat ramps
    '''
    # api call that I will not be using, I am going to switch to google maps api in future release
    response = requests.get('https://data.nashville.gov/resource/xbru-cfzi.json/')
    launch_data = response.json()
    length_data = len(launch_data)
    sliced = launch_data[0:122:1]
    ramp_data = ''
    canoe_data = ''
    boat_launch = ''
    go_launch = ''
    park_name = ''
    query = request.GET.get('q')
    if query == None:
        q_str = 'near+me'
    elif query != None:
        q_str = str(query)

    for idx in range(0, len(sliced)):

        # ramp_data = sliced[idx]['boat_launch']
        canoe_data = sliced[idx]['canoe_launch']
        park_name += sliced[idx]['mapped_location_address'] + " "
        boat_launch = canoe_data + ramp_data
        if "Yes" in boat_launch:
            for x in boat_launch:
                go_launch = str(park_name + ' ')
    return render(request, 'launch.html', {'q_str': q_str, 'length_data': length_data, 'sliced': sliced})


