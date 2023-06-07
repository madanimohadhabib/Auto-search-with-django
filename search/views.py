from django.http import JsonResponse
from django.shortcuts import render
from .models import Names

def index(request):
    return render(request,'search.html')

def get_names(request):
    search = request.GET.get('search')
    payload = []
    if search:
        objs = Names.objects.filter(name__startswith = search)
        
        for obj in objs :
            payload.append({
                'name' : obj.name
            })
        
    return JsonResponse({
            'status' : True,
            'payload': payload
        })