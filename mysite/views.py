# I have created this page - 'rajnish'
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.GET.get('text','default')
    removepuch = request.GET.get('removepuch', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    newlineremove=request.GET.get('newlineremove', 'off')
    extraspaceremove=request.GET.get('extraspaceremove', 'off')
    charcount=request.GET.get('charcount', 'off')
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepuch == 'on':
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if uppercase == 'on':
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Convert all To UPPER Case', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if newlineremove=='on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyzed = analyzed + char
        params = {'purpose': 'Remove all new line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if extraspaceremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove all Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcount =='on':
        count= len(djtext)
        params = {'purpose': 'The no of characters in this text are', 'analyzed_text': count}

    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")

def about(request):
    return HttpResponse('''<h1>tel me about your self</h1> <a href="https://www.geeksforgeeks.org">www.geeksforgeeks.org </a>''')