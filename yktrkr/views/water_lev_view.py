from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
import operator
from django.db.models import Q
import requests
import json
import numpy as np
import os
# just rendering a search form
def search_form(request):

    return render(request, 'levels.html')
# accessing the USGS NWSI database
def water_levels(request):
    # initial api call
    response = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    large_data = level_data_raw['value']
    site_name_2 = (large_data['timeSeries'])
    # limiting results to 500 for demo day
    sliced = site_name_2[0:500:1]
    # predefining variables for later use
    one_level_further = ''
    one_level_further_stage = ''
    one_level_further_deets =''
    final_data = ''
    site_name = ''
    water_level = ''
    measurment_type = ''
    just_name = ''
    # creating a variable to hold search input
    query = request.GET.get('q')


    # filtering down to the keys needed from USGS api
    for idx in range(0, len(sliced)):

         one_level_further = sliced[idx]['sourceInfo']['siteName']
         one_level_further_stage = sliced[idx]['values'][0]['value'][0]['value']
         one_level_further_deets = sliced[idx]['variable']['variableName']
        # combining filtered data
         combo_data = one_level_further + ': ' + one_level_further_deets + ' '
         final_data = combo_data + one_level_further_stage + ' '
        # comparing filterd data to search input. if match present return results
         if str(query) in final_data:
            # for x in final_data:
                idx_num = str(idx)
                site_name = str(final_data)
                just_name = str(one_level_further_stage)
                measurment_type += str(one_level_further_deets)






    return render(request, 'levels.html', {'site_name': site_name, 'just_name': just_name, 'measurment_type': measurment_type, 'large_data': large_data})

