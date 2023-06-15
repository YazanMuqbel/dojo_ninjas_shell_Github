from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Dojo, Ninja

# Create your views here.
def home(request):
    data = dict(
        dojos = Dojo.objects.all(),
        ninjas = Ninja.objects.all()
    )
    return render(request, 'dojo_ninjas_app/index.html', context=data)


def create_ninja(request):
    if request.method == 'POST':
        params = dict()
        
        params['first_name'] = request.POST.get('first')
        params['last_name'] = request.POST.get('last')
        params['dojo_id'] = request.POST.get('dojo')
        
        dojo = Dojo.objects.get(id=params['dojo_id'])
        if dojo:
            Ninja.objects.create(**params)
            #Ninja.save()

    return redirect(reverse('app-home'))    

def create_dojo(request):
    if request.method == 'POST':
        params = dict()
        
        params['name'] = request.POST.get('name')
        params['city'] = request.POST.get('city')
        params['state'] = request.POST.get('state')
        params['desc'] = request.POST.get('desc')
        
        Dojo.objects.create(**params)
    return redirect(reverse('app-home'))    

def delete_dojo(request, pk):
    dojo = Dojo.objects.get(id=pk)
    if dojo:
        dojo.delete()
    return redirect(reverse('app-home'))

