
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request,'index.html')
def analyse(request):
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','default')
    removenumber = request.POST.get('removenumber', 'default')
    newlineremover = request.POST.get('newlineremover','default')
    extraspaceremover = request.POST.get('extraspaceremover','default')
    charactercounter = request.POST.get('charactercounter', 'default')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
               analysed = analysed + char
        params = {'purpose': 'removed punctuations ','analysed_text': analysed}
        djtext = analysed
        # return render(request,'Analyse.html',params)

    if removenumber == "on":
        numbers = "0123456789"
        analysed = ""
        for char in djtext:
            if char not in numbers:
                analysed = analysed + char
        params = {'purpose': 'removed numbers', 'analysed_text': analysed}
        djtext = analysed

    if newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char
        params = {'purpose': 'removed newlines', 'analysed_text': analysed}
        djtext = analysed

    if extraspaceremover == "on":
        analysed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed = analysed + char
        params = {'purpose': 'removed extra space ', 'analysed_text': analysed}
        djtext = analysed

    if charactercounter == "on":
        count = 0
        for char in djtext:
            if char != " ":
                count += 1
        analysed = str(count)
        params = {'purpose': 'character counts', 'analysed_text': analysed}

    if(removepunc != "on" and newlineremover != "on" and removenumber != "on" and extraspaceremover != "on" and charactercounter != "on"):
        return HttpResponse("error")

    return render(request, 'Analyse.html', params)