from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
import operator
from django.db.models import Q
import requests
import json

# this just loads the weather.html template
def weather (request):
    '''
    this does nothing but render a template
    '''

    return render(request, 'weather.html')