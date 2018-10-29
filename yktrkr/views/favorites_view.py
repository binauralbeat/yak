from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
import operator
from django.db.models import Q
import requests
import json
from django.contrib.auth import logout, login, authenticate
from collections import defaultdict
import os



from yktrkr.models.site_model import Site
from yktrkr.models.profile_account import *
# this is one method of saving sites that I did not finish. however I plan on going back and using it eventually when scaling up

def fav (request):
    site_name = request.POST.get('site_name')
    site = Site(site_name=site_name, user_id=request.user.id)
    site.save()

    return render(request, 'index.html', {})

def favs_post (request):
    # the following is for getting the api data
    response = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    # print(level_data_raw)
    large_data = level_data_raw['value']
    site_name_2 = (large_data['timeSeries'])
    sliced = site_name_2[0:500:1]
    # bellow is for getting the db data
    water = ''
    sites = []
    sites = Site.objects.filter(user = request.user.id)
    stream = []
    for site in sites:
        stream.append(site)
        for u in stream:
            water = u.site_name
            print(water, 'line39')






# these are for later use
    one_level_further = ''
    one_level_further_stage = ''
    one_level_further_deets =''
    final_data = ''
    site_name = ''
    water_level = ''
    measurment_type = ''
    site_list = []
    site_level = ''
    # print(sites)



# bellow is for digging into api to level of desired data
    for idx in range(0, len(sliced)):
         data_list = []
         one_level_further = sliced[idx]['sourceInfo']['siteName']
         one_level_further_stage = sliced[idx]['values'][0]['value'][0]['value']
         one_level_further_deets = sliced[idx]['variable']['variableName']
        # combining api data into one variable
         combo_data = one_level_further + ': ' + one_level_further_deets + ' '
         final_data = combo_data + one_level_further_stage + ' '
        #  sending data to list
         for l in final_data:
            data_list.append(final_data)
            # print(data_list)
         stream_list = []
        #  print(final_data
        # making list of api data
         for site in sites :
            # if str(site) in one_level_further:
            #    for a in one_level_further_stage:
            #        site_level = [a]
                #    site_list.append(one_level_further_stage)
            if str(site) in one_level_further:
               for a in one_level_further_stage:
                   site_level = [a]
                   site_list.append(site_level)



    # print(site_list)

    return render(request, 'favorites_list.html', {'site_list': site_list,'stream': stream, 'final_data': final_data})

def favorite_delete_view(request, pk):
    '''
    this is a function that deletes streams from favorites
    '''

    stream = get_object_or_404(Site, pk=pk)
    stream.delete()
    return redirect('yktrkr:favorite_list')

# @register.filter(name='user_name_filter')
# def user_name_filter()