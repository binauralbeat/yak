from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
import operator
from django.db.models import Q
import requests
import json


def boat_ramps (request):
    response = requests.get('https://data.nashville.gov/resource/xbru-cfzi.json/')
    launch_data = response.json()
    length_data = len(launch_data)
    sliced = launch_data[0:122:1]
    ramp_data = ''
    canoe_data = ''
    boat_launch = ''
    go_launch = ''
    park_name = ''
    for idx in range(0, len(sliced)):

        # ramp_data = sliced[idx]['boat_launch']
        canoe_data = sliced[idx]['canoe_launch']
        park_name += sliced[idx]['mapped_location_address'] + " "
        boat_launch = canoe_data + ramp_data
        if "Yes" in boat_launch:
            for x in boat_launch:
                go_launch = str(park_name + ' ')
    return render(request, 'launch.html', {'go_launch': go_launch, 'length_data': length_data, 'sliced': sliced})


