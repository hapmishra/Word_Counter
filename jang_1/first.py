from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,"about.html")
def count(request):
    text=request.GET['fulltext']
    # print(text)
    word=text.split()
    length_of_words=(len(word))
    worddictionay={}
    for word in word:
        if word in worddictionay:
            worddictionay[word] +=1
        else:
            worddictionay[word] =1
    return render(request,'Count.html',{"fulltext":text,"count":length_of_words,"dict":worddictionay.items()})