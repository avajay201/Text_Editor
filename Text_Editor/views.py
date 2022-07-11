from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from Text_Editor.models import Contact
import string



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
    newlineremove = request.POST.get('newlineremove', 'off')
    espaceremove = request.POST.get('espaceremove', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    charcount = request.POST.get('charcount', 'off')
    boldtext = request.POST.get('boldtext', 'off')
    italictext = request.POST.get('italictext', 'off')
    Str = request.POST.get('str', 'off')
    Int = request.POST.get('int', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    charcount = request.POST.get('charcount', 'off')
    spacecount = request.POST.get('spacecount', 'off')
    strcount = request.POST.get('strcount', 'off')
    intcount = request.POST.get('intcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    params = {}
    if removepunc == 'on':
        result = ""
        for char in djtext:
            if char not in punctuations:
                result = result + char
        djtext = result
        params = {'purpose': 'Remove Puncuations', 'result': result}
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
    if uppercase == 'on':
        result = ""
        for char in djtext:
            result = result + char.upper()
        djtext = result
        params = {'purpose': 'Changed To Uppercase', 'result': result}
    if lowercase == 'on':
        result = ""
        for char in djtext:
            result = result + char.lower()
        djtext = result
        params = {'purpose': 'Changed To Uppercase', 'result': result}
    if boldtext == 'on':
        result = djtext
        params = {'purpose': 'Bold', 'result': result}
    if italictext == 'on':
        result = djtext
        params = {'purpose': 'Italic', 'result': result}     
    if Str == 'on':
        result = ""
        for char in djtext:
            if not(char in string.digits):
                result = result + char  
        params = {'purpose': 'String', 'result': result}     
    if Int == 'on':
        djtext = djtext.lower()
        result = ""
        for char in djtext:
            if not(char in string.ascii_lowercase):
                result = result + char  
        params = {'purpose': 'Integer', 'result': result}
    if capitalize == 'on':
        result = djtext.capitalize()
        params = {'purpose': 'Capitalize', 'result': result}
    if charcount == 'on':
        result = len(djtext)
        params = {'purpose': 'Character Count', 'result': result}
    if spacecount == 'on':
        result = ""
        for char in djtext:
            if char == " ":
                result = result + char
        result = len(result)
        params = {'purpose': 'Character Count', 'result': result}
    if strcount == 'on':
        djtext = djtext.lower()
        result = ""
        for char in djtext:
            if char in string.ascii_lowercase:
                result = result + char
        result = len(result)        
        params = {'purpose': 'Character Count', 'result': result}
    if intcount == 'on':
        result = ""
        for char in djtext:
            if char in string.digits:
                result = result + char
        result = len(result) 
        params = {'purpose': 'Character Count', 'result': result}
    if len(djtext) < 1:
        messages.warning(request, 'Please write your texts!')
        return render(request, 'index.html')
    if not(removepunc == 'on' or newlineremove == 'on' or espaceremove == 'on' or uppercase == 'on' or lowercase == 'on' or charcount == 'on' or boldtext == 'on' or italictext == 'on' or Str == 'on' or Int == 'on' or capitalize == 'on' or charcount == 'on' or spacecount == 'on' or strcount == 'on' or intcount == 'on'):
        messages.warning(request, 'Please turn on atleast one function!')
        return render(request, 'index.html')
    return render(request, 'result.html', params)
