from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    return render(request , 'index.html')

def analyze(request):
    djtext = (request.POST.get('text','default'))
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase' , 'off')
    lowercase = request.POST.get('lowercase','off')
    newLineRemover = request.POST.get('newLineRemover','off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover', 'off')

    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuation','analyzed_text':analyzed}
        return render(request , 'analyze.html', params)
    elif uppercase == 'on' :
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Upper Case','analyzed_text':analyzed}
        return render(request , 'analyze.html', params)
    elif lowercase == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose':'lower Case','analyzed_text':analyzed}
        return render(request , 'analyze.html', params)
    elif newLineRemover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'Remove New Lines','analyzed_text':analyzed}
        return render(request , 'analyze.html', params)
    elif extraSpaceRemover == 'on':
        analyzed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char;
        params = {'purpose':'Remove extra spaces','analyzed_text':analyzed}
        return render(request , 'analyze.html', params)    
    else:
        return HttpResponse('error')