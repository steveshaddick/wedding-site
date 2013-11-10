from django.shortcuts import render

# Create your views here.
def form(request):
	response = render(
        request,
        'wedding_rsvp/form.html',
        {
            
        }
    )