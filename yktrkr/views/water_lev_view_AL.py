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
def water_levels_AL(request):
    # initial api call
    response = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=al&parameterCd=00065&siteType=ST&siteStatus=all')
    print(response)
    level_data_raw = response.json()
    large_data_AL = level_data_raw['value']
    site_name_AL_2 = (large_data_AL['timeSeries'])
    print (len(site_name_AL_2))
    # limiting results to 500 for demo day
    sliced = site_name_AL_2[0:156:1]
    # predefining variables for later use
    one_level_further = ''
    one_level_further_stage = ''
    one_level_further_deets =''
    final_data = ''
    site_name_AL = []
    site_level_AL = []
    water_level = ''
    measurment_type_AL = ''
    just_name = ''
    site_list_AL = []
    stage_list = []
    # creating a variable to hold search input
    query = request.GET.get('q')


    # filtering down to the keys needed from USGS NWIS api
    for idx in range(0, len(sliced)):

         one_level_further = [sliced[idx]['sourceInfo']['siteName']]
         if str(query) in str(one_level_further):
            # site_name_AL.append(one_level_further)
            for a in one_level_further:
                # print (a)
                site_name_AL = [a]
         one_level_further_stage = [sliced[idx]['values'][0]['value'][0]['value']]
        #  print(one_level_further_stage)
         if str(query) in str(one_level_further):
            print(one_level_further)
            # site_level_AL.append(one_level_further_stage)
            for a in one_level_further_stage:
                # print (a)
                site_level_AL = [a]
                site_list_AL.append(one_level_further + one_level_further_stage)
            #   print(site_list_AL)


         one_level_further_deets = [sliced[idx]['variable']['variableName']]
        # combining filtered data
         combo_data = [one_level_further] +  [one_level_further_deets ]
         final_data = [combo_data] + [one_level_further_stage ]
        #  print(final_data)
        # comparing filterd data to search input. if match present return results
         if str(query) in final_data:
            for x in final_data:
                idx_num = str(idx)
                # site_name_AL = str(final_data)
                # print(site_name_AL)

                just_name = str(one_level_further_stage)
                measurment_type_AL += str(one_level_further_deets)






    return render(request, 'levels.html', {'site_list_AL': site_list_AL, 'site_name_AL': site_name_AL, 'site_level_AL': site_level_AL, 'measurment_type_AL': measurment_type_AL, 'large_data_AL': large_data_AL})



