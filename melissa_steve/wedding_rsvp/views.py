from django.shortcuts import render

# Create your views here.
def form(request):
	return render(
        request,
        'wedding_rsvp/form.html',
        {
            
        }
    )