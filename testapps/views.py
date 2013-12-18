from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

def index(request):
  return HttpResponse("Testapp index listing.")

def show(request, testapp_id):
  return HttpResponse("Showing testapp %s" % testapp_id)

def slashed(request, testapp_id):
  return HttpResponse("Showing testapp %s at url that should be / terminated." % testapp_id)