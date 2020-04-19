from django.shortcuts import render
from .models import WhatToDo

def index(request):
    things = WhatToDo.objects.first()
    return render(request,'myapp/index.html',{'things':things})

def next(request,thing_id):
    last = WhatToDo.objects.last()
    things = WhatToDo.objects.get(pk=thing_id+1)
    if last == things:
        things = WhatToDo.objects.get(pk=2)  #pk 2 because i deleted 1st object

        return render(request,'myapp/index.html',{'things':things})      
    else:    
        return render(request,'myapp/index.html',{'things':things})
    
    
   
        

    
   
    
