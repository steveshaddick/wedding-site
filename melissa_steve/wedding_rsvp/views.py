from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render

from models import WeddingRSVP

import os, json


def json_response(success, response={}):
    
    if (success is False):
        if ('error' not in response):
            response['error'] = 'General error.'
        response['success'] = False
    else:
        response['success'] = True

    return HttpResponse(json.dumps(response), mimetype='application/json')


# Create your views here.
def form(request):
	return render(
        request,
        'wedding_rsvp/form.html',
        {
            
        }
    )


def submit(request):

	attending = request.POST['rdoAttending']
	names = request.POST['txtNames']
	dietary_restrictions = request.POST['txtDiet']

	rsvp = WeddingRSVP.create(
		attending=(attending=='yes'),
		names=names,
		dietary_restrictions=dietary_restrictions
	)
	rsvp.save()

	return json_response(True)