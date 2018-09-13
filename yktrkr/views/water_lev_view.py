from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
import operator
from django.db.models import Q
import requests
import json
import numpy as np

def search_form(request):
    '''
	Author: Meghan Debity
	Purpose: Input form for search bar feature
	'''
    return render(request, 'levels.html')

def water_levels(request):
    response = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    large_data = level_data_raw['value']
    site_name_2 = (large_data['timeSeries'])
    sliced = site_name_2[0:300:1]
    one_level_further = ''
    one_level_further_stage = ''
    one_level_further_deets =''
    final_data = ''
    site_name = ''
    water_level = ''
    measurment_type = ''
    query = request.GET.get('q')


    for idx in range(0, len(sliced)):

         one_level_further = sliced[idx]['sourceInfo']['siteName']
         one_level_further_stage = sliced[idx]['values'][0]['value'][0]['value']
         one_level_further_deets = sliced[idx]['variable']['variableName']

         combo_data = one_level_further + ': ' + one_level_further_deets + ' '
         final_data = combo_data + one_level_further_stage + ' '

         if str(query) in final_data:

            idx_num = str(idx)
            site_name += (final_data)
            water_level += str(one_level_further_stage)
            measurment_type += str(one_level_further_deets)




    return render(request, 'levels.html', {'site_name': site_name, 'water_level': water_level, 'measurment_type': measurment_type, 'large_data': large_data})

