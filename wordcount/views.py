from django.http import HttpResponse
from django.shortcuts import render
import re
import operator

def home(request):
    return render(request, 'homepage.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    #cleaned_wordlist = []

    for each in wordlist:
        if re.match(r'^\w', each):
            stripped_word = each.rstrip(',')
            if each in worddictionary:
                worddictionary[each] +=1
            else:
                worddictionary[each] = 1

    cleaned_wordlist = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'words':cleaned_wordlist, 'fulltext': fulltext})


def about(request):
    return render(request, 'about.html')
