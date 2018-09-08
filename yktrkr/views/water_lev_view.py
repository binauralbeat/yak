from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
import requests
import json


def water_levels(request):
    response = requests.get('http://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00060,00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    large_data = level_data_raw['value']
    site_name_2 = (large_data['timeSeries'])
    level_data = (level_data_raw['value']['timeSeries'][350]['sourceInfo']['siteName'])
    level_data_stage = (level_data_raw['value']['timeSeries'][350]['values'][0]['value'][0]['value'])
    data_deets = (level_data_raw['value']['timeSeries'][350]['variable']['variableName'])
    site_name = str(level_data)
    water_level =str(level_data_stage)
    measurment_type =str(data_deets)


    return render(request, 'levels.html', {'site_name': site_name, 'water_level': water_level, 'measurment_type': measurment_type, 'large_data': large_data})

