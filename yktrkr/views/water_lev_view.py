from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
import requests
import json
import numpy as np


def water_levels(request):
    response = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    large_data = level_data_raw['value']
    # new_large_data = np.asarray()
    site_name_2 = (large_data['timeSeries'])
    sliced = site_name_2[0:100:1]
    # first_fifty_slice = slice(50, None)
    one_level_further = ''
    one_level_further_stage = ''
    one_level_further_deets =''
    final_data = ''
    for idx in range(0, len(sliced)):

         one_level_further = sliced[idx]['sourceInfo']['siteName']
         one_level_further_stage = sliced[idx]['values'][0]['value'][0]['value']
         one_level_further_deets = sliced[idx]['variable']['variableName']

         combo_data = one_level_further + ': ' + one_level_further_deets + ' '
         final_data += combo_data + one_level_further_stage + '    '




    level_data = (level_data_raw['value']['timeSeries'][49]['sourceInfo']['siteName'])
    level_data_stage = (level_data_raw['value']['timeSeries'][49]['values'][0]['value'][0]['value'])
    data_deets = (level_data_raw['value']['timeSeries'][49]['variable']['variableName'])


    idx_num = str(idx)
    site_name = str(final_data)
    water_level = str(one_level_further_stage)
    measurment_type = str(one_level_further_deets)


    return render(request, 'levels.html', {'idx_num': idx_num,'site_name': site_name, 'water_level': water_level, 'measurment_type': measurment_type, 'large_data': large_data})

