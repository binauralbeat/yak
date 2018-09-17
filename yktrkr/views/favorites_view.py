from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
import operator
from django.db.models import Q
import requests
import json
from django.contrib.auth import logout, login, authenticate



from yktrkr.models.site_model import Site
from yktrkr.models.profile_account import *


def fav(request):
    site_name = request.POST.get('site_name')
    site = Site(site_name=str(site_name), user_id=request.user.id)
    site.save()

    return render(request, 'index.html', {})

def favs_post(request):
    response = requests.get('https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&stateCd=tn&parameterCd=00065&siteType=ST&siteStatus=all')
    level_data_raw = response.json()
    large_data = level_data_raw['value']
    site_name_2 = (large_data['timeSeries'])
    sliced = site_name_2[0:500:1]
    sites = Site.objects.all()
    one_level_further = ''
    one_level_further_stage = ''
    one_level_further_deets =''
    final_data = ''
    site_name = ''
    water_level = ''
    measurment_type = ''
    print(sliced)

    for idx in range(0, len(sliced)):

         one_level_further = sliced[idx]['sourceInfo']['siteName']
         one_level_further_stage = sliced[idx]['values'][0]['value'][0]['value']
         one_level_further_deets = sliced[idx]['variable']['variableName']

         combo_data = one_level_further + ': ' + one_level_further_deets + ' '
         final_data = combo_data + one_level_further_stage + ' '
    if sites.site_name in final_data:
        site_list = final_data
    template_name = 'index.html'
    print(site_list)
    return render(request, template_name, {'site_list': site_list})

# def favs(request):
#     if request.is_ajax():
#      if request.method == 'GET':
#         site = Site.objects.get(id=request.GET.get('userid'))
#         site.site_name = request.GET.get('siteName')
#         site.save()
#         return render(request, 'levels.html',)


