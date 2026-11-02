


# i created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("""
    #     <h1 style='background-color: red; COLOR:BLUE;'>
    #     SEEMA DEVI <BR>
    #     AMAN IS MONKEY
        
    #     </h1>
    #     """)
    return render(request,'INDEX.HTML')

