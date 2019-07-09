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
import re
# just rendering a search form
def search_form(request):

    return render(request, 'levels.html')
# accessing the USGS NWSI database
def water_levels(request):
    # initial api call
    response = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=TN&parameterCd=00065&siteStatus=active')

    level_data_raw = response.json()
    large_data = level_data_raw['value']
    site_name_2 = (large_data['timeSeries'])
    print (len(site_name_2))
    # limiting results to 500 for demo day
    sliced = site_name_2[0:156:1]
    # predefining variables for later use
    one_level_further = ''
    one_level_further_stage = ''
    one_level_further_deets =''
    final_data = ''
    site_name = []
    site_level = []
    water_level = ''
    measurment_type = ''
    just_name = ''
    site_list = []
    stage_list = []
    # creating a variable to hold search input
    query = request.GET.get('q')
    q_upper =str(query).upper()


    # filtering down to the keys needed from USGS NWIS api
    for idx in range(0, len(sliced)):

         one_level_further = [sliced[idx]['sourceInfo']['siteName']]
         if str(q_upper) in str(one_level_further):
            # site_name.append(one_level_further)
            for a in one_level_further:
                # print (a)
                site_name = [a]
         one_level_further_stage = [sliced[idx]['values'][0]['value'][0]['value']]
        #  print(one_level_further_stage)
         one_level_further_deets = [sliced[idx]['variable']['variableName']]
         if str(q_upper) in str(one_level_further):
            print(one_level_further)
            # site_level.append(one_level_further_stage)
            for a in one_level_further_stage:
                # print (a)
                site_level = [a]
                site_list.append(one_level_further + one_level_further_stage + one_level_further_deets)
            #   print(site_list)

        #  elif str(query) not in str(one_level_further):
        #      site_list = [["Sorry, we couldn't find anything."]]



        # combining filtered data
         combo_data = [one_level_further] +  [one_level_further_deets ]
         final_data = [combo_data] + [one_level_further_stage ]
        #  print(final_data)
        # comparing filterd data to search input. if match present return results
         if str(q_upper) in final_data:
            for x in final_data:
                idx_num = str(idx)
                # site_name = str(final_data)
                # print(site_name)

                just_name = str(one_level_further_stage)
                measurment_type += str(one_level_further_deets)






    return render(request, 'levels.html', {'site_list': site_list, 'site_name': site_name, 'site_level': site_level, 'measurment_type': measurment_type, 'large_data': large_data})



