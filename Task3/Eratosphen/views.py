from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def simple_num(request, id):
    number = int(id)
    prime = [x for x in range(number + 1)]
    prime[0] = prime[1] = 0
    lst = []
    i = 2
    while i <= number:
        if prime[i] != 0:
            lst.append(prime[i])
            for j in range(i, number + 1, i):
                prime[j] = 0
        i += 1

    return render(request, 'simple_num.html', {'nums':lst})