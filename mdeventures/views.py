from django.shortcuts import render
from .models import *
# Create your views here.

def getdata(x):

    task = Tasks.objects.get(id = x.id)
    try:
        logs = task.logs_set.all().latest('end_time')
        status = logs.status
    except:
        logs = 'No Data'
        status = 'No Data'
    context = {'data':logs,'status':status}
    return context
    
def home(request):

    MD_D = Tasks.objects.filter(merchant='MD', frequency = 'D' ) 
    MD_M = Tasks.objects.filter(merchant='MD', frequency = 'M' )
   

    MD_Daily = []
    MD_Monthly = []
  
    
    for x in MD_D:
        data = getdata(x)
        MD_Daily.append(data)
    
    for x in MD_M:
        data = getdata(x)
        MD_Monthly.append(data)
    
  
    MD_Daily = sorted(MD_Daily, key=lambda k: k['status']) 
    MD_Monthly = sorted(MD_Monthly, key=lambda k: k['status'])
   
    
    context = {'MD_Daily':MD_Daily, 'MD_Monthly':MD_Monthly}

    return render(request, 'mdeventures/pages/md_status.html', context)


def bnl(request):

    
    BNL_D = Tasks.objects.filter(merchant='BNL', frequency = 'D' )
    BNL_M = Tasks.objects.filter(merchant='BNL', frequency = 'M' )

   
    BNL_Daily = []
    BNL_Monthly = []
    
   
    for x in BNL_D:
        data = getdata(x)
        BNL_Daily.append(data)
    
    for x in BNL_M:
        data = getdata(x)
        BNL_Monthly.append(data)

  
    BNL_Daily = sorted(BNL_Daily, key=lambda k: k['status'])
    BNL_Monthly = sorted(BNL_Monthly, key=lambda k: k['status'])
    
    context = {'BNL_Daily':BNL_Daily, 'BNL_Monthly':BNL_Monthly}

    return render(request, 'mdeventures/pages/bnl_status.html', context)
