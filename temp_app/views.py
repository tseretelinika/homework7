
from django.shortcuts import render


def home(request):
    return render(request, 'info.html', {
        'first_name': 'nika',
        'last_name': 'tsereteli',
        'age': 15,
        'height': 188,
    })


def hobbies(request):
    context = {
        'hobbies': ['Coding', 'Football', 'Gaming', 'Gym'],
        'grade': 10,
    }
    return render(request, 'hobbies.html', context)
