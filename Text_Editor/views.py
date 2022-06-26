from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from Text_Editor.models import Contact


def index(request):
    messages.success(request, 'You can edit your texts here!')
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        if len(name) >= 3 and len(query) >= 10:
            contacts = Contact(name=name, email=email, query=query)
            contacts.save()
            messages.success(request, "Successfully, Sent your message.")
        else:
            messages.error(request, "Please fill correct data!")
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    espaceremove = request.POST.get('espaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    params = {} 
    if len(djtext) == 0:
        messages.warning(request, "Please write your text!")
        return render(request, 'index.html')
    if not(removepunc == 'on' or fullcaps == 'on' or newlineremove == 'on' or espaceremove == 'on' or charcount == 'on'):
        messages.warning(request, 'Please turn on atleast one function!')
        return render(request, 'index.html')    
    if removepunc == 'on':
        result = ""
        for char in djtext:
            if char not in punctuations:
                result = result + char
        djtext = result
        params = {'purpose': 'Remove Puncuations', 'result': result}
    if fullcaps == 'on':
        result = ""
        for char in djtext:
            result = result + char.upper()
        djtext = result
        params = {'purpose': 'Changed To Uppercase', 'result': result}
    if newlineremove == 'on':
        result = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                result = result + char
        djtext = result
        params = {'purpose': 'NewLine Removed', 'result': result}
    if espaceremove == 'on':
        result = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                result = result + char
        djtext = result
        params = {'purpose': 'Extra Space Removed', 'result': result}
    if charcount == 'on':
        result = len(djtext)
        params = {'purpose': 'Chaarcters Count', 'result': result}
    return render(request, 'result.html', params)