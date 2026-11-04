


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

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)

    print(djtext)
    if removepunc == "on":
    # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    #Analyze the text
                return render(request, 'analyze.html', params)
            else:
                return HttpResponse("Error") 

