


# i created this file
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1 style='background-color: red; COLOR:BLUE;'>
        SEEMA DEVI <BR>
        AMAN IS MONKEY
        
        </h1>
        """)

