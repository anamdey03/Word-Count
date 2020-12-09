import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hello')
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()
    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sorted_word = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    context = {
        'text': text,
        'count': len(wordlist),
        'word_dictionary': sorted_word
    }
    return render(request, 'count.html', context)
