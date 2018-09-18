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



from yktrkr.models.site_model import Site
from yktrkr.models.profile_account import *


def fav (request):
    site_name = request.POST.get('site_name')
    site = Site(site_name=site_name, user_id=request.user.id)
    site.save()

    return render(request, 'index.html', {})

def favs_post (request):
    # the following is for getting the api data
    response = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    large_data = level_data_raw['value']
    site_name_2 = (large_data['timeSeries'])
    sliced = site_name_2[0:500:1]
    # bellow is for getting the db data
    sites = Site.objects.all()
    stream = []
    for site in sites:
        stream.append(site)
        for u in stream:
            water = u.site_name
            print(water, 'line 45')





# these are for later use
    one_level_further = ''
    one_level_further_stage = ''
    one_level_further_deets =''
    final_data = ''
    site_name = ''
    water_level = ''
    measurment_type = ''
    site_list = ''
    # print(sites)



# bellow is for digging into api to level of desired data
    for idx in range(0, len(sliced)):

         one_level_further = sliced[idx]['sourceInfo']['siteName']
         one_level_further_stage = sliced[idx]['values'][0]['value'][0]['value']
         one_level_further_deets = sliced[idx]['variable']['variableName']

         combo_data = one_level_further + ': ' + one_level_further_deets + ' '
         final_data = combo_data + one_level_further_stage + ' '
        #  print(final_data)
         if str(water) in final_data:
            site_list = final_data
            print(site_list, '79')

    # print(site_list)

    return render(request, 'favorites_list.html', {'stream': stream})

def favorite_delete_view(request, pk):

    stream = get_object_or_404(Site, pk=pk)
    stream.delete()
    return redirect('yktrkr:levels')
