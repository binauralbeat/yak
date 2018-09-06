from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
import requests


def water_levels(request):
    response = requests.get('http://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00060,00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    level_data = str(level_data_raw['value']['timeSeries']['sourceInfo']['siteName'])
    site_name = level_data


    return render(request, 'levels.html', {'site_name': site_name})

