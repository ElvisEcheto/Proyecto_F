from django.shortcuts import render, redirect

from rservices.models import Rservice

from .forms import LodgingForm

def create_lodging(request):
    form = LodgingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lodgings')    
    return render(request, 'lodgings/create.html', {'form': form})

def rservices(request):    
    rservices_list = Rservice.objects.all()    
    return render(request, 'rservices/index.html', {'rservices_list': rservices_list})

def change_status_rservice(request, rservice_id):
    rservice = Rservice.objects.get(pk=rservice_id)
    rservice.status = not rservice.status
    rservice.save()
    return redirect('rservices')