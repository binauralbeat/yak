from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
import requests
import json


def water_levels(request):
    response = requests.get('http://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00060,00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    level_data = (level_data_raw['value']['timeSeries'][0]['sourceInfo']['siteName'])

    site_name = str(level_data)


    return render(request, 'levels.html', {'site_name': site_name})

