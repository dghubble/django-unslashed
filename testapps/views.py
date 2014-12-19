from django.http import HttpResponse

def index(request):
    return HttpResponse("Testapp index listing.")

def show(request, testapp_id):
    return HttpResponse("Showing testapp %s" % testapp_id)

def slashed(request, testapp_id):
    return HttpResponse("Showing testapp %s at url that should be / terminated." % testapp_id)

def plused(request):
    return HttpResponse("Showing URLs with plus signs are not re-encoded")

def quoted(request):
    return HttpResponse("Showing URLs with url-encoding are not re-encoded")
